from fastapi import FastAPI

app = FastAPI()

books = [
{
        "id": 1,
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "year": 1937
    },
    {
        "id": 2,
        "title": "1984",
        "author": "George Orwell",
        "year": 1949
    },
    {
        "id": 3,
        "title": "Harry Potter",
        "author": "J.K. Rowling",
        "year": 1997
    },
    {
        "id": 4 ,
        "title": "Crime And Punishment",
        "author": "Fyodor dustayofski",
        "year": 1886
    },
    {
        "id": 5 ,
        "title": "Don Quixote",
        "author": "Miguel de Cervantes",
        "year": 1605
    }
]

@app.get("/books")
def get_books():
    return books



@app.get("/books/{book_id}")
def get_the_books(book_id:int):
    for book in books:
        if book["id"] == book_id :
           return book
    else:
        return {"message": "Book Not Found"}

@app.post("/books")
def add_books(book:dict):
    new_book = {
        "id": len(books) + 1 ,
        "title": book["title"] ,
        "author": book["author"] ,
        "year": book["year"]
    }
    books.append(new_book)
    return new_book




@app.put("/books/{book_id}")
def change_book_detail(book_id:int , updated_book:dict):
    for book in books:
        if book["id"] == book_id:
            book["title"] = updated_book["title"]
            book["author"] = updated_book["author"]
            book["year"] = updated_book["year"]
            return book
    else:
        return {"message" : "Book not Found"}
        
        


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {
                "message": "Book deleted successfully"
            }
    return {
        "message": "Book not found"
    }