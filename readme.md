## 🛠️ Quick Start
1. Install dependencies: `pip install -r requirements.txt`
2. Run the server: `python app.py`
3. The database `library.db` will be created automatically.


# Online Book Rental Management System (Backend)

## 🚀 Project Overview
This is a robust backend system designed to manage book inventories, user registrations, and rental transactions. Developed as part of the Backend Developer Intern assessment.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Framework:** Flask / FastAPI / Django (as requested)
- **Database:** SQLite (for easy portability) or MySQL
- **Tools:** Postman for API testing

## 📊 Database Design
The system utilizes a relational database with three primary tables:
1. **Users:** Stores member information (ID, Name, Email).
2. **Books:** Tracks inventory (ID, Title, Author, Availability Status).
3. **Rentals:** Links users to books with transaction details.

## ✨ Implemented Features
- **Book Management:** Add new books and view current inventory.
- **User Management:** Register new users and list active members.
- **Rental Logic:** - Rent a book (updates status to unavailable).
    - Return a book (updates status to available).
    - View all currently rented books.
- **Bonus Features:** Due date tracking and rental history logging.

## 🚦 API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /users | Register a new user |
| GET | /books | View all books |
| POST | /books | Add a new book |
| POST | /rent | Rent a book (ID-based) |
| POST | /return | Return a book |
