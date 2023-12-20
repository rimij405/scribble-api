from typing import Union

from fastapi import FastAPI

# Define the application.
app = FastAPI()

@app.get("/")
async def home():
    return { "Hello": "World" }

@app.get("/notes/{note_id}")
async def view_note(note_id: int, q: Union[str, None] = None):
    return {
        "note_id": note_id,
        "q": q
    }