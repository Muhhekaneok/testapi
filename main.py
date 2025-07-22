from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()


class Book(BaseModel):
    title: str = Field(..., min_length=3)
    author: str
    pages: int = Field(..., ge=20)


books_db = []


@app.post("/books/")
def create_book(book: Book):
    books_db.append(book)
    return {"message": f"Book {book.title} was created successfully", "book": book}


@app.get("/books/")
def get_all_books():
    return {"books": books_db}


@app.get("/books/{book_id}")
def get_book(book_id: int):
    if book_id < 0 or book_id >= len(books_db):
        raise HTTPException(status_code=404, detail="Book not found")
    return books_db[book_id]


@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    if book_id < 0 or book_id >= len(books_db):
        raise HTTPException(status_code=404, detail="Book not found")
    books_db[book_id] = updated_book
    return {"message": f"Book {book_id} updated successfully", "book": updated_book}


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    if book_id < 0 or book_id >= len(books_db):
        raise HTTPException(status_code=404, detail="Book not found")
    deleted_book = books_db.pop(book_id)
    return {"message": f"Book {book_id} deleted successfully", "book": deleted_book}
