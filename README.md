# Library Management System - DjangoREST

This is a DjangoREST application for managing a library system. It provides CRUD (Create, Read, Update, Delete) operations for books.

## Features

- Allows listing all books
- Allows adding a new book
- Supports updating an existing book
- Supports deleting a book

## Installation

1. Clone the repository:


2. Navigate to the project directory:



3. Create a virtual environment (optional but recommended): python -m venv venv


4. Activate the virtual environment:

- On Windows: venv\Scripts\activate



- On macOS and Linux: source venv/bin/activate


5. Install the dependencies: pip install -r requirements.txt


6. Create environment variables using the `env_template` file



7. Run migrations to create database tables: python manage.py migrate


8. Run the development server: python manage.py runserver


9. Access the API endpoints in your browser or using tools like Postman:

    http://127.0.0.1:8000/api/books/ # Endpoint for adding and listing books
    http://127.0.0.1:8000/api/books/<id>/ # Endpoint for updating and deleting a book


## API Endpoints

- `POST /api/books/`: Create a new book
- `GET /api/books/`: Retrieve all books 
- `PUT /api/books/<id>/`:  Update book by ID
- `GET /api/books/<id>/`: Retrieve a book by ID
- DELETE /api/books/<id>/`:  Delete book by ID

## Technologies Used

- Django
- Django REST Framework (DRF)
- SQLite: Database system used for development


## Testing

Unit tests have been included to verify the functionality of the application. To run the tests, execute the following command:
      `python manage.py test`




