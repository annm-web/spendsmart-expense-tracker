# Expense Tracker

Personal expense tracking web app built with FastAPI and plain HTML/JS.

## How to Run

1. Install dependencies:
pip install fastapi uvicorn pydantic

2. Start the server:
uvicorn main:app --reload

3. Open browser at:
http://127.0.0.1:8000

## Stack Choices
- Backend: FastAPI (Python) — chose because I know Python well
- Frontend: Plain HTML + JavaScript — no framework needed for this scope
- Database: JSON file — simple, no setup required, runs locally

## What's Done
- Add expense with title, amount, category, date, note
- View all expenses sorted by date (most recent first)
- Edit any expense
- Delete any expense
- Monthly summary with total and category breakdown
- Filter by category, date range, and title search
- Date defaults to today
- Validates required fields before saving

## What's Skipped
- Authentication — not required per spec
- Deployment — runs locally as required
- Test suite — not required per spec
- Multi-currency — not required per spec

## Known Limitations
- Data stored in JSON file, lost if file is deleted
- No multi-user support
- Basic UI styling