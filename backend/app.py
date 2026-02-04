from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from backend.rag_core import answer_question, load_model

app = FastAPI(
    title="Safe RAG Chatbot",
    version="1.0"
)

# CORS FIX (VERY IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class QuestionRequest(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    answer: str
    source: str

@app.on_event("startup")
def startup():
    load_model()

@app.get("/")
def root():
    return {"status": "Backend running"}

@app.post("/ask", response_model=AnswerResponse)
def ask(req: QuestionRequest):
    return answer_question(req.question)
