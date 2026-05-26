from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional
from datetime import date
import json
import os

app = FastAPI()

DATA_FILE = "expenses.json"

def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f)

expenses = load_expenses()

class Expense(BaseModel):
    title: str
    amount: float
    category: str
    date: str
    note: Optional[str] = ""

@app.get("/", response_class=HTMLResponse)
def home():
    with open("index.html") as f:
        return f.read()

@app.get("/expenses")
def get_expenses(category: Optional[str] = None,
                  title: Optional[str] = None,
                  from_date: Optional[str] = None,
                  to_date: Optional[str] = None):
    result = expenses
    if category:
        result = [e for e in result if e["category"] == category]
    if title:
        result = [e for e in result if title.lower() in e["title"].lower()]
    if from_date:
        result = [e for e in result if e["date"] >= from_date]
    if to_date:
        result = [e for e in result if e["date"] <= to_date]
    return sorted(result, key=lambda x: x["date"], reverse=True)

@app.post("/expenses")
def add_expense(expense: Expense):
    new_expense = expense.dict()
    new_expense["id"] = len(expenses) + 1
    expenses.append(new_expense)
    save_expenses(expenses)
    return new_expense

@app.put("/expenses/{expense_id}")
def update_expense(expense_id: int, expense: Expense):
    for i, e in enumerate(expenses):
        if e["id"] == expense_id:
            expenses[i] = expense.dict()
            expenses[i]["id"] = expense_id
            save_expenses(expenses)
            return expenses[i]
    return {"message": "not found"}

@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):
    for i, e in enumerate(expenses):
        if e["id"] == expense_id:
            expenses.pop(i)
            save_expenses(expenses)
            return {"message": "deleted"}
    return {"message": "not found"}

@app.get("/summary")
def monthly_summary():
    today = date.today()
    current_month = today.strftime("%Y-%m")
    monthly = [e for e in expenses if e["date"].startswith(current_month)]
    total = sum(e["amount"] for e in monthly)
    breakdown = {}
    for e in monthly:
        breakdown[e["category"]] = breakdown.get(e["category"], 0) + e["amount"]
    return {"total": total, "breakdown": breakdown, "month": current_month}