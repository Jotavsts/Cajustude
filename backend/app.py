from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from summarizer import Summarizer

app = FastAPI()
summarizer = Summarizer()

class TextRequest(BaseModel):
    text: str

@app.post("/summarize")
async def summarize_text(request: TextRequest):
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Texto vazio")
    summary = summarizer.summarize(request.text)
    return {"summary": summary}
