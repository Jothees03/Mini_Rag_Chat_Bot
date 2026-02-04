import re
import requests
from pathlib import Path
from transformers import pipeline

# ===============================
# PATHS
# ===============================
BASE_DIR = Path(__file__).resolve().parent
LOCAL_DOC_PATH = BASE_DIR / "data" / "documents.txt"

# ===============================
# CONFIG
# ===============================
SEARCH_API = "https://en.wikipedia.org/w/api.php"
SUMMARY_API = "https://en.wikipedia.org/api/rest_v1/page/summary/"
USER_AGENT = "SafeWikiRAG/DocAware"

STOP_WORDS = {
    "tell", "something", "about", "who", "is", "how",
    "what", "the", "me", "please", "explain", "give"
}

MAX_WIKI_CHARS = 1200
MIN_SUMMARY_LEN = 120
MAX_NEW_TOKENS = 120

# ===============================
# LOAD MODEL ONCE
# ===============================
llm = None

def load_model():
    global llm
    if llm is None:
        print("🔄 Loading LLM model...")
        llm = pipeline(
            "text2text-generation",
            model="google/flan-t5-small",
            device=-1
        )
        print("✅ LLM loaded")

# ===============================
# LOAD DOCUMENTS (DOC_ID FORMAT)
# ===============================
def load_documents():
    documents = []

    print(f"📄 Loading documents from: {LOCAL_DOC_PATH}")

    if not LOCAL_DOC_PATH.exists():
        print("❌ documents.txt not found")
        return documents

    content = LOCAL_DOC_PATH.read_text(encoding="utf-8")

    blocks = re.split(r"\[DOC_ID:\d+\]", content)
    blocks = [b.strip() for b in blocks if b.strip()]

    for idx, block in enumerate(blocks, start=1):
        documents.append({
            "id": idx,
            "text": block
        })

    print(f"✅ Loaded {len(documents)} documents")
    return documents

DOCUMENTS = load_documents()

# ===============================
# CLEAN QUERY
# ===============================
def clean_query(text: str) -> str:
    words = re.findall(r"\w+", text.lower())
    return " ".join(w for w in words if w not in STOP_WORDS)

# ===============================
# SEARCH DOCUMENTS (LOCAL FIRST)
# ===============================
def search_documents(cleaned_query: str):
    query_words = set(cleaned_query.split())

    best_score = 0
    best_doc = None

    for doc in DOCUMENTS:
        doc_words = set(re.findall(r"\w+", doc["text"].lower()))
        score = len(query_words & doc_words)

        if score > best_score:
            best_score = score
            best_doc = doc["text"]

    if best_score > 0:
        return best_doc

    return None

# ===============================
# WIKIPEDIA SEARCH
# ===============================
def wikipedia_search(query: str):
    params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "format": "json"
    }
    headers = {"User-Agent": USER_AGENT}

    try:
        res = requests.get(SEARCH_API, params=params, headers=headers, timeout=5)
        data = res.json()
        for r in data.get("query", {}).get("search", []):
            if not r["title"].lower().startswith("list of"):
                return r["title"]
    except:
        return None

# ===============================
# WIKIPEDIA SUMMARY
# ===============================
def wikipedia_summary(title: str):
    headers = {"User-Agent": USER_AGENT}
    try:
        res = requests.get(
            SUMMARY_API + title.replace(" ", "_"),
            headers=headers,
            timeout=5
        )
        text = res.json().get("extract", "")
        if len(text) < MIN_SUMMARY_LEN:
            return None
        return text[:MAX_WIKI_CHARS]
    except:
        return None

# ===============================
# FORMAT ANSWER (NO HALLUCINATION)
# ===============================
def summarize(text: str):
    load_model()
    prompt = f"""
Answer using ONLY the information below.
Do NOT add new facts.

Text:
{text}

Answer:
"""
    return llm(prompt, max_new_tokens=MAX_NEW_TOKENS, do_sample=False)[0]["generated_text"]

# ===============================
# MAIN RAG FUNCTION
# ===============================
def answer_question(question: str):
    cleaned = clean_query(question)

    # 🔐 STEP 1: DOCUMENTS FIRST
    doc_text = search_documents(cleaned)
    if doc_text:
        return {
            "answer": summarize(doc_text),
            "source": "local_document"
        }

    # 🌍 STEP 2: WIKIPEDIA
    title = wikipedia_search(cleaned)
    if not title:
        return {
            "answer": "I don’t have reliable information.",
            "source": "none"
        }

    summary = wikipedia_summary(title)
    if not summary:
        return {
            "answer": "I don’t have reliable information.",
            "source": "none"
        }

    return {
        "answer": summarize(summary),
        "source": "wikipedia"
    }
