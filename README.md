# FastAPI Demo

This project is a simple full-stack demo built with FastAPI for the backend and React for the frontend.

## Project Overview

- Backend: FastAPI with SQLAlchemy and SQLite.
- Frontend: React app created with Create React App.
- Purpose: Demonstrate a basic product management API with a React user interface.

## How the Project Was Created

1. Backend created with Python and FastAPI.
2. SQLAlchemy used to define database models and connect to a SQLite database.
3. Pydantic used for request and response validation.
4. Frontend created as a React application using Create React App.
5. Axios is used on the frontend to make HTTP requests to the FastAPI backend.

## Technologies Used

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite
- React
- Create React App
- Axios
- Uvicorn
- JavaScript

## Project Structure

- `main.py` - FastAPI application and route definitions.
- `database.py` - SQLAlchemy engine and session configuration.
- `database_models.py` - SQLAlchemy ORM model definitions.
- `models.py` - Pydantic model definitions for request validation.
- `requirements.txt` - Python dependencies.
- `frontend/` - React frontend application.

## Workflow

1. Start the backend server using Uvicorn.
2. Start the frontend React app.
3. The React app sends HTTP requests to the backend using the configured proxy.
4. The backend handles requests, performs database operations, and returns data as JSON.
5. CRUD operations are supported for products: create, read, update, delete.

## Running the Project

### Backend

1. Create and activate a Python virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the FastAPI app:
   ```bash
   uvicorn main:app --reload
   ```

### Frontend

1. Change to the frontend folder:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the React development server:
   ```bash
   npm start
   ```

## Notes

- The frontend proxy is configured to `http://127.0.0.1:8000` so React API calls are forwarded to the FastAPI backend.
- The backend initializes default product data if the database is empty.
- CORS is enabled for development.
