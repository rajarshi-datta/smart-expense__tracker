# Smart Expense Tracker API

A REST API built with **FastAPI** to manage personal expenses. This application allows users to add, view, filter, calculate totals, and delete expenses. Expense data is stored in a local JSON file, so no database is required.

---

## Features

- Add a new expense
- View all expenses
- Filter expenses by category
- Calculate total expenses
- Calculate total expenses by category
- Delete an expense
- Interactive API documentation using **Swagger/OpenAPI** (Bonus Feature)

---

## Tech Stack

- Python 3.12+
- FastAPI
- Pydantic
- Pytest
- Uvicorn
- JSON File Storage

---

## Project Structure

```
Smart_expense_tracker/
│
├── README.md
├── AI_NOTES.md
├── requirements.txt
├── .gitignore
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── routes.py
│   ├── storage.py
│   └── expenses.json
│
└── tests/
    ├── __init__.py
    └── test_api.py
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/rajarshi-datta/smart-expense__tracker.git
cd smart-expense__tracker
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows (PowerShell)**

```powershell
venv\Scripts\Activate.ps1
```

**Windows (Command Prompt)**

```cmd
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Server

Start the FastAPI application:

```bash
uvicorn src.main:app --reload
```

The server will start at:

```
http://127.0.0.1:8000
```

---

## API Documentation (Bonus Feature)

Interactive Swagger UI:

```
http://127.0.0.1:8000/docs
```

OpenAPI Specification:

```
http://127.0.0.1:8000/openapi.json
```

---

## Available API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/expenses` | Add a new expense |
| GET | `/expenses` | View all expenses |
| GET | `/expenses/category/{category}` | Filter expenses by category |
| GET | `/expenses/total` | Get total expenses |
| GET | `/expenses/total/{category}` | Get total expenses for a category |
| DELETE | `/expenses/{expense_id}` | Delete an expense |

---

## Example Request

### Add Expense

**POST** `/expenses`

```json
{
    "title": "Lunch",
    "amount": 250,
    "category": "Food",
    "date": "2026-08-01"
}
```

Example Response

```json
{
    "title": "Lunch",
    "amount": 250,
    "category": "Food",
    "date": "2026-08-01",
    "id": 1
}
```

---

## Running Tests

Run the automated test suite:

```bash
pytest
```

Expected output:

```
===== 5 passed =====
```

---

## Data Storage

Expenses are stored locally in:

```
src/expenses.json
```

No external database is required.

---

## Optional Bonus Implemented

**OpenAPI / Swagger Documentation**

FastAPI automatically generates interactive API documentation that allows all endpoints to be tested directly from the browser.

---

## Author

**Rajarshi Datta**

Software Engineering Apprenticeship Assignment – Diligent (2026)