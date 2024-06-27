# FastAPI CRUD API

This project is a simple RESTful API for managing a collection of items. It supports operations for creating, retrieving, updating, and deleting items using FastAPI, Pydantic, and SQLite.

## Project Structure

- `main.py`: The entry point of the application, contains the FastAPI app and routes.
- `schemas.py`: Defines the Pydantic models for request and response bodies.
- `database.py`: Manages the SQLite database connection.
- `models.py`: Defines the SQLAlchemy models for the database tables.

## Setup Instructions

Follow these steps to set up and run the project locally.

### Prerequisites

- Python 3.7+
- pip (Python package installer)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/PhanaiPundisondQualyfi/FastAPI-Lab.git
    cd FastAPI-Lab
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

### Running the API

1. **Start the FastAPI server:**

    ```bash
    uvicorn main:app --reload
    ```

2. **Access the API documentation:**

    Open your web browser and navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to see the interactive API documentation.

## API Endpoints

### Create a new item

- **URL:** `/items/`
- **Method:** `POST`
- **Request Body:**

    ```json
    {
        "name": "Item Name",
        "description": "Item Description",
        "price": 9.99,
        "tax": 0.5
    }
    ```

- **Response:**

    ```json
    {
        "id": 1,
        "name": "Item Name",
        "description": "Item Description",
        "price": 9.99,
        "tax": 0.5
    }
    ```

### Retrieve all items

- **URL:** `/items/`
- **Method:** `GET`
- **Response:**

    ```json
    [
        {
            "id": 1,
            "name": "Item Name",
            "description": "Item Description",
            "price": 9.99,
            "tax": 0.5
        }
    ]
    ```

### Retrieve an item by ID

- **URL:** `/items/{item_id}`
- **Method:** `GET`
- **Response:**

    ```json
    {
        "id": 1,
        "name": "Item Name",
        "description": "Item Description",
        "price": 9.99,
        "tax": 0.5
    }
    ```

### Update an item by ID

- **URL:** `/items/{item_id}`
- **Method:** `PUT`
- **Request Body:**

    ```json
    {
        "name": "Updated Item Name",
        "description": "Updated Item Description",
        "price": 19.99,
        "tax": 1.0
    }
    ```

- **Response:**

    ```json
    {
        "id": 1,
        "name": "Updated Item Name",
        "description": "Updated Item Description",
        "price": 19.99,
        "tax": 1.0
    }
    ```

### Delete all items

- **URL:** `/items/`
- **Method:** `DELETE`
- **Response:**

    ```json
    {
        "detail": "All items deleted"
    }
    ```

### Delete an item by ID

- **URL:** `/items/{item_id}`
- **Method:** `DELETE`
- **Response:**

    ```json
    {
        "detail": "Item deleted"
    }
    ```

## Testing the API

You can use a REST client extension in VSCode or tools like Postman to test the API endpoints.
