from typing import Union

from fastapi import FastAPI
# from fastapi.staticfiles import StaticFiles
from fastapi.exceptions import RequestValidationError
from fastapi.responses import FileResponse

# Define the application.
app = FastAPI()

# Mount the static files directory.
# app.mount("/assets", StaticFiles(directory="assets"), name="assets")
# app.mount("/public", StaticFiles(directory="public"), name="public")

@app.exception_handler(404)
async def error_404(_, __):
    return FileResponse("./public/404.html", 404)

@app.exception_handler(RequestValidationError)
async def error_422(_, __):
    return FileResponse("./public/422.html", 422)

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("./assets/favicon.png")

@app.get("/backend")
async def home():
    return { "Hello": "World" }

@app.get("/backend/notes/{note_id}")
async def view_note(note_id: int, q: Union[str, None] = None):
    return {
        "note_id": note_id,
        "q": q
    }