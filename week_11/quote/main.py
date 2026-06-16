from fastapi import FastAPI, HTTPException

from pydantic import BaseModel
from typing import List

app = FastAPI(title="Citates")

class Quote(BaseModel):
    quote: str
    author: str

class QuoteOut(Quote):
    id: int

quotes_db = []
quote_id_counter = 1

@app.get("/quotes", response_model=List[QuoteOut])
def get_all_quotes():
    return quotes_db

@app.post("/quotes", status_code=201, response_model=QuoteOut)
def add_quote(
    quote: Quote
):
    global quote_id_counter
    new_quote = quote.model_dump()
    new_quote["id"] = quote_id_counter
    quote_id_counter += 1
    quotes_db.append(new_quote)
    return new_quote

@app.get("/quotes/{quote_id}", response_model=QuoteOut)
def get_quote(
    quote_id: int
):
    for quote in quotes_db:
        if quote["id"] == quote_id:
            return quote
    raise HTTPException(status_code=404, detail="Quote not found")

@app.delete("/quote/{quote_id}")
def delete_quote(
    quote_id: int
):
    for i, quote in enumerate(quotes_db):
        if quote["id"] == quote_id:
            quotes_db.pop(i)
            return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Quote not found")