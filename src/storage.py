import json
import os

BASE_DIR = os.path.dirname(__file__)
FILE_NAME = os.path.join(BASE_DIR, "expenses.json")

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as f:
        json.dump([], f)

def load_expenses():
    with open(FILE_NAME, "r") as f:
        return json.load(f)

def save_expenses(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)