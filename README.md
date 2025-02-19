# Student Management System

A full-stack project built for Datalogz, showcasing the management of students, courses, and enrollments. This README outlines the project architecture, APIs and setup instructions.

---

## Table of Contents
1. [Project Overview](#project-overview)  
2. [Tech Stack](#tech-stack)  
3. [Features & Endpoints](#features--endpoints)  
4. [Backend Details](#backend-details)  
5. [Setup Instructions](#setup-instructions)  
6. [How to Run Locally](#how-to-run-locally)  


---

## Project Overview
This application allows users to:
- **Manage Students** (Create, Retrieve)  
- **Manage Courses** (Create, Retrieve)  
- **Enroll Students** in courses and view enrolled courses.  

The project was developed as part of the Datalogz assignment, demonstrating **backend** (FastAPI) skills.

---

## Tech Stack
- **Backend**: FastAPI (Python)  
- **Database**: PostgreSQL (using SQLAlchemy + Alembic for migrations)  
- **Authentication**: JWT-based authentication (using `python-jose`)  
- **Other Libraries**:  
  - `pytest` + `pytest-asyncio` for testing  
  - `Pydantic` for data validation  
  - `Alembic` for database migrations  

---

## Features & Endpoints

### Authentication
- **POST** `/token`  
  - **Body**: `username`, `password` (using `OAuth2PasswordRequestForm`)  
  - **Response**: `{"access_token": "<token>", "token_type": "bearer"}`  

### Students
- **POST** `/students/`  
  - **Request Body**:  
    ```json
    {
      "name": "string",
      "age": 21,
      "email": "string"
    }
    ```
  - **Response**: Created student object  
  - **Authentication**: Required

- **GET** `/students/{student_id}`  
  - **Response**: Student object  
  - **Authentication**: Required

### Courses
- **POST** `/courses/`  
  - **Request Body**:  
    ```json
    {
      "title": "string",
      "description": "string"
    }
    ```
  - **Response**: Created course object  
  - **Authentication**: Required

- **GET** `/courses/{course_id}`  
  - **Response**: Course object  
  - **Authentication**: Required

### Enrollments
- **POST** `/enrollments/`  
  - **Request Body**:  
    ```json
    {
      "student_id": "int",
      "course_id": "int"
    }
    ```
  - **Response**: `{"message": "Enrollment successful"}`  
  - **Authentication**: Required

- **GET** `/student/{student_id}/courses`  
  - **Response**: `{"enrolled_courses": [course_ids]}`  
  - **Authentication**: Required

---

## Backend Details
- **Framework**: FastAPI  
- **ORM**: SQLAlchemy (with async support)  
- **Migrations**: Alembic for versioning database schema changes.  
- **Authentication**:  
  - **JWT** tokens created by `create_access_token`.  
  - **Protected Endpoints**: Require `Bearer <token>` in the `Authorization` header.  
- **Tests**:  
  - **Pytest** + **TestClient** for synchronous endpoints  
  - **pytest-asyncio** for asynchronous tests (if needed)

---

## Setup Instructions

1. **Clone the Repo**  
   ```bash
   git clone <https://github.com/SarangShelke2304/Datalogz>

2. **Create a virtual env**
   ```bash
   python -m venv venv
   source venv/bin/activate   # or venv\Scripts\activate on Windows

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt

4. **Environment Variables**
   
   Create a .env file or set environment variables for:

    ```bash
    DATABASE_URL (e.g., postgresql+asyncpg://user:password@host:port/dbname)
    JWT_SECRET_KEY (any secure string)

5. **Running Locally**

    Start the FastAPI server
   ```bash
   uvicorn app.main:app --reload
   
6. **Access the API docs on:**
  
    ```bash
    http://127.0.0.1:8000/docs
