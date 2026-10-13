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

@app.get("/books/{book_id}")
def get_the_books(book_id:int):
    for book in Data:
        if Data[id] == book_id :
           return book
    else:
        return {"message": "Book Not Found"}

@app.post("/books")
def add_books():
    new_book = {
        "id": len(Data) + 1 ,
        "title": book.title ,
        "author": book.author ,
        "year": book.year
    }
    
    Data.append(new_book)
    return new_book

@app.put("/books/{book_id}")
def change_book_detail(book_id:int , updated_book:Data):
    for book in Data:
        if Data["id"] == book_id:
            Data["title"] = updated_Data.title
            Data["author"] = updated_Data.author
            Data["year"] = updated_Data.year
            return book
        else:
            return {"message" : "Book not Found"}
    