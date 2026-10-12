from FastAPI import fastapi

app = fastapi()

Data = [
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
    return Data

@app.get("/books/{book_id :int}")
def get_the_books(id):
    for book in Data:
        if Data[id] == book_id :
           return book
    else:
        return {"message": "Book Not Found"}