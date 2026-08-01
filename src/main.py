from fastapi import FastAPI
from .routes import router

app = FastAPI(title="Smart Expense Tracker API")

app.include_router(router)