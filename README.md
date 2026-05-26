# SpendSmart - Expense Tracker

A personal expense tracking web app built with FastAPI and HTML/JS.

## How to Run

1. Install dependencies:
pip install fastapi uvicorn pydantic

2. Start the server:
uvicorn main:app --reload

3. Open browser at:
http://127.0.0.1:8000

## Stack
- Backend: FastAPI (Python)
- Frontend: Plain HTML + JavaScript
- Storage: JSON file (no database setup needed)

## Features
- Add expense with title, amount, category, date, note
- View all expenses sorted by date
- Edit and delete expenses
- Monthly summary with category breakdown
- Filter by category, date range, and title search

## What's Skipped
- Authentication (not required)
- Deployment (runs locally)
- Test suite (not required)

## Known Limitations
- Data stored in JSON file
- No multi-user support