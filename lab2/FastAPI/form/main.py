from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class TextRequest(BaseModel):
    text: str
    operation: str  # upper, lower, capitalize, title

@app.post("/format")
def format_text(request: TextRequest):
    if request.operation == "upper":
        return {"formatted_text": request.text.upper()}
    elif request.operation == "lower":
        return {"formatted_text": request.text.lower()}
    elif request.operation == "capitalize":
        return {"formatted_text": request.text.capitalize()}
    elif request.operation == "title":
        return {"formatted_text": request.text.title()}
    else:
        return {"error": "Invalid operation"}
    
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)