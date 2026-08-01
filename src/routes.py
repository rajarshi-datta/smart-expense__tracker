from fastapi import APIRouter, HTTPException
from .models import Expense, ExpenseCreate
from .storage import load_expenses, save_expenses
router = APIRouter()
@router.post("/expenses", response_model=Expense)
def add_expense(expense: ExpenseCreate):
    expenses = load_expenses()

    new_expense = Expense(
        id=max((e["id"] for e in expenses), default=0) + 1,
        title=expense.title,
        amount=expense.amount,
        category=expense.category,
        date=expense.date,
    )

    expense_data = new_expense.model_dump(mode="json")

    expenses.append(expense_data)
    save_expenses(expenses)

    return new_expense
@router.get("/expenses")
def get_expenses():
    return load_expenses()
@router.get("/expenses/category/{category}")
def filter_category(category: str):
    expenses = load_expenses()
    filtered = [
    expense
    for expense in expenses
    if expense["category"].lower() == category.lower()
]
    return filtered
@router.get("/expenses/total")
def total():
    expenses = load_expenses()
    total_amount = sum(expense["amount"] for expense in expenses)
    return {"total": total_amount}
@router.get("/expenses/total/{category}")
def category_total(category: str):
    expenses = load_expenses()
    total = sum(
    expense["amount"]
    for expense in expenses
    if expense["category"].lower() == category.lower()
)
    return {
    "category": category,
    "total": total
}

@router.delete("/expenses/{expense_id}")
def delete(expense_id: int):
    expenses = load_expenses()

    for expense in expenses:
        if expense["id"] == expense_id:
            expenses.remove(expense)
            save_expenses(expenses)
            return {"message": "Expense deleted"}

    raise HTTPException(
        status_code=404,
        detail="Expense not found"
    )