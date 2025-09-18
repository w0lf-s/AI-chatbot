from fastapi import FastAPI
from pydantic import BaseModel
from langgraph_workflow import build_workflow

app = FastAPI()
chatbot = build_workflow()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(request: ChatRequest):
    response = chatbot(request.message)
    return {"response": response}
