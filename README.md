# 🔐 Safe RAG Chatbot
# Local Documents First · Wikipedia Fallback · No Hallucinations

A **Retrieval-Augmented Generation (RAG)** chatbot that **strictly prioritizes local documents** before falling back to **Wikipedia**, ensuring **accurate, grounded, and non-hallucinated answers**.

This project demonstrates a **production-style RAG architecture** using **FastAPI** and a lightweight chatbot frontend built with **HTML, CSS, and JavaScript**.

---

## 🚀 Key Features

- ✅ Local-first retrieval (documents are always checked first)
- ✅ Supports unstructured documents ([DOC_ID:x] format)
- ✅ No hallucinations (LLM answers only from retrieved text)
- ✅ Wikipedia used only as fallback
- ✅ FastAPI backend with Swagger UI
- ✅ Modern green + black chatbot UI
- ✅ Source attribution (local_document / wikipedia)
- ✅ Beginner-friendly and extensible design

---

## 🧠 What Is RAG?

Retrieval-Augmented Generation (RAG) is an AI technique where:
1. Relevant documents are retrieved first
2. An LLM generates answers only using those documents

This prevents:
- Guessing
- Fabricated answers
- Hallucinations

This project implements true RAG behavior, not search-only or LLM-only answering.

---

## 🔄 RAG Workflow

User Question
      ↓
Clean & Normalize Query
      ↓
Search Local Documents (Mandatory)
      ↓
If Found → Answer from Document
      ↓
Else → Search Wikipedia
      ↓
Safe Summarization
      ↓
Final Answer + Source
---

## 📄 Document Format

Local knowledge is stored in backend/data/documents.txt using the following format:

[DOC_ID:1]
ReValix is an AI-powered real estate analytics platform.
It helps users analyze property values and investment potential.

[DOC_ID:2]
Retrieval-Augmented Generation (RAG) is an AI technique
that retrieves documents before generating answers.

Why this format?
- Simple to write
- Human-readable
- No strict schema
- Works across multiple domains (AI, health, sports, etc.)

---

## 🛠️ Tech Stack

Backend:
- Python 3.10+
- FastAPI
- Uvicorn
- Hugging Face Transformers
- Requests

Frontend:
- HTML
- CSS
- Vanilla JavaScript

---

## ⚙️ Setup Instructions

### Create Virtual Environment
python -m venv .venv

Activate it (Windows):
.venv\Scripts\activate

Activate it (Linux / macOS):
source .venv/bin/activate

---

### Install Dependencies
pip install -r requirements.txt

---

## ▶️ Run the Backend

uvicorn backend.app:app --host 127.0.0.1 --port 3448

Swagger UI:
http://127.0.0.1:3448/docs

---

## ▶️ Run the Frontend

cd frontend
python -m http.server 5500

Open in browser:
http://127.0.0.1:5500

---

## 💬 Example Queries

- what is revalix        → Local Document
- what is rag            → Local Document
- what is faiss          → Local Document
- ipl                    → Local Document
- chennai super kings    → Local Document
- ms dhoni               → Wikipedia
- virat kohli            → Wikipedia

---

## 🔌 API Usage

Endpoint:
POST /ask

Request:
{
  "question": "what is rag"
}

Response:
{
  "answer": "Retrieval-Augmented Generation (RAG) is an AI technique that retrieves documents first and then generates answers based on that information.",
  "source": "local_document"
}

---

## 🔍 Why This Project Is Safe

- No uncontrolled LLM output
- No guessing
- No hallucinated facts
- Answers are grounded in retrieved text
- Clear source attribution
- Deterministic and explainable behavior

---

## 🧪 How to Verify Local-First Behavior

1. Add a topic to documents.txt
2. Ask the same question in the chatbot
3. Confirm:
   Source: local_document

Wikipedia should NOT be used if a document exists.

---

## 🧩 Future Enhancements

- FAISS vector embeddings (semantic search)
- Multiple document citations
- Confidence scoring
- Chat memory
- Authentication / API keys
- Docker & cloud deployment
- Streaming responses

---

## 🧠 Interview-Ready Summary

“I built a local-first RAG chatbot using FastAPI that retrieves answers from a document corpus before falling back to Wikipedia, ensuring accuracy and preventing hallucinations.”

---

## 👤 Author

Jotheeswaran  
AI & ML Developer

---

## 📜 License

This project is intended for learning, demonstration, and portfolio use.
You are free to modify and extend it.

---

⭐ If you found this project useful, consider starring the repository!
