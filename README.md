# Simple Library FastAPI

This is a simple Library API built with **Python** and **FastAPI**.

The project is made for learning the basic concepts of FastAPI and working with APIs.

For now, the book data is stored in a Python list, so no database is used.

## Features

The API can:

- Get all books
- Get a specific book by ID
- Add a new book
- Update a book
- Delete a book

## Technologies

- Python
- FastAPI
- Uvicorn
- uv

## Book Data

Each book contains the following information:

```json
{
    "id": 1,
    "title": "The Hobbit",
    "author": "J.R.R. Tolkien",
    "year": 1937
}
```

## API Endpoints

### Get All Books

```http
GET /books
```

Returns all books in the library.

### Get a Specific Book

```http
GET /books/{book_id}
```

Example:

```http
GET /books/1
```

Returns the book with ID `1`.

### Add a New Book

```http
POST /books
```

Example request:

```json
{
    "title": "The Lord of the Rings",
    "author": "J.R.R. Tolkien",
    "year": 1954
}
```

The book ID is created automatically.

### Update a Book

```http
PUT /books/{book_id}
```

Example:

```http
PUT /books/1
```

Example request:

```json
{
    "title": "The Hobbit Updated",
    "author": "J.R.R. Tolkien",
    "year": 1937
}
```

### Delete a Book

```http
DELETE /books/{book_id}
```

Example:

```http
DELETE /books/3
```

Deletes the book with ID `3`.

## Running the Project

Run the following command:

```bash
python3.15 -m uv run uvicorn simple_library_fastapi.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## API Documentation

FastAPI automatically provides API documentation using Swagger UI.

You can open it here:

```text
http://127.0.0.1:8000/docs
```

From this page, you can test the GET, POST, PUT, and DELETE requests.

## Note

The current version does not use a database. The books are stored in a Python list.

This means that changes made to the books will be lost when the application is restarted.

## Project Goal

The main goal of this project is to learn the basics of FastAPI and understand how different API methods work:

- GET
- POST
- PUT
- DELETE
- Path Parameters
- Request Body
