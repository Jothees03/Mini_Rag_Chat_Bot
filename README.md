
# 🔐 Safe RAG Chatbot (Local Documents + Wikipedia)

A **Retrieval-Augmented Generation (RAG)** chatbot that **strictly prioritizes local documents** before falling back to **Wikipedia**, ensuring **accurate, non-hallucinated answers**.

This project demonstrates a **real-world RAG architecture** using:

* FastAPI backend
* Local document retrieval
* Wikipedia fallback
* Lightweight LLM summarization
* Pure HTML/CSS/JavaScript frontend chatbot

---

## 🚀 Features

* ✅ **Local-first RAG** (documents are always checked first)
* ✅ Supports **unstructured documents** (`[DOC_ID:x]` format)
* ✅ **No hallucinations** (answers generated only from retrieved text)
* ✅ Wikipedia used **only as fallback**
* ✅ FastAPI backend with Swagger UI
* ✅ Modern green & black chatbot UI
* ✅ Works fully offline for local documents
* ✅ Beginner-friendly and extensible

---

## 🧠 How the RAG Pipeline Works

1. **User asks a question**
2. The system:

   * Cleans the query
   * Searches **local documents first**
   * Finds the most relevant document using keyword overlap
3. If a local document is found:

   * The answer is generated **only from that document**
4. If no document matches:

   * Wikipedia is queried
   * A short, safe summary is generated
5. The response is returned with a **clear source label**

```
Local Documents → Wikipedia → No Answer
        ↑
     Priority
```

---

## 📁 Project Structure

```
mini_rag_project/
│
├── backend/
│   ├── __init__.py
│   ├── app.py                 # FastAPI application
│   ├── rag_core.py            # RAG logic (local-first)
│   └── data/
│       └── documents.txt      # Knowledge base
│
├── frontend/
│   ├── index.html             # Chatbot UI
│   ├── style.css              # Green + Black theme
│   └── script.js              # API integration
│
├── requirements.txt
└── README.md
```

---

## 📄 Document Format (`documents.txt`)

Documents are stored as **unstructured blocks**:

```text
[DOC_ID:1]
ReValix is an AI-powered real estate analytics platform.
It helps users analyze property values and investment potential.

[DOC_ID:2]
Retrieval-Augmented Generation (RAG) is an AI technique
that retrieves documents first before generating answers.
```

* No fixed keys required
* Supports mixed topics (AI, health, sports, etc.)
* Easily extensible

---

## 🛠️ Tech Stack

### Backend

* **Python 3.10+**
* **FastAPI**
* **Uvicorn**
* **Hugging Face Transformers**
* **Requests**

### Frontend

* **HTML**
* **CSS**
* **JavaScript (Vanilla)**

---

## ⚙️ Installation & Setup

### 1️⃣ Create Virtual Environment

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Backend

From the project root:

```bash
uvicorn backend.app:app --host 127.0.0.1 --port 3448
```

* Swagger UI:
  👉 [http://127.0.0.1:3448/docs](http://127.0.0.1:3448/docs)

---

## ▶️ Run the Frontend

Open a new terminal:

```bash
cd frontend
python -m http.server 5500
```

Open in browser:

👉 [http://127.0.0.1:5500](http://127.0.0.1:5500)

---

## 💬 Example Queries

| Question             | Source Used    |
| -------------------- | -------------- |
| `what is revalix`    | Local Document |
| `what is rag`        | Local Document |
| `what is faiss`      | Local Document |
| `ipl`                | Local Document |
| `ms dhoni`           | Wikipedia      |
| `who is virat kohli` | Wikipedia      |

---

## 🧪 API Example

### Request

```http
POST /ask
Content-Type: application/json

{
  "question": "what is rag"
}
```

### Response

```json
{
  "answer": "Retrieval-Augmented Generation (RAG) is an AI technique that retrieves relevant documents first and then generates answers based on that information.",
  "source": "local_document"
}
```

---

## 🔍 Why This Project Is Safe

* ❌ No free-text hallucination
* ❌ No uncontrolled LLM responses
* ✅ Answers are grounded in retrieved text
* ✅ Clear source attribution
* ✅ Deterministic behavior

---

## 🧩 Future Improvements

* 🔹 FAISS vector embeddings (semantic search)
* 🔹 Confidence scoring
* 🔹 Multiple document citations
* 🔹 Chat history memory
* 🔹 Authentication / API keys
* 🔹 Docker deployment
* 🔹 Cloud hosting

---

## 🧠 Interview-Ready Summary

> “I built a local-first RAG chatbot using FastAPI that retrieves answers from a document corpus before falling back to Wikipedia, ensuring accuracy and preventing hallucinations.”

---

## 📜 License

This project is for **learning and demonstration purposes**.
You are free to modify and extend it.

---
