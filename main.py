import os
import datetime as dt
import pandas as pd

# ---------- Constants ----------
FILE_NAME = "expenses.csv"
COLUMNS = ["date", "category", "amount", "notes"]


# ---------- Helper functions ----------
def load_data():
    """Load the CSV file into a DataFrame (or return an empty one)."""
    if not os.path.exists(FILE_NAME):
        return pd.DataFrame(columns=COLUMNS)
    return pd.read_csv(FILE_NAME)


def save_data(df):
    """Save the DataFrame to the CSV file."""
    df.to_csv(FILE_NAME, index=False)


def get_valid_amount(prompt="Amount: "):
    """Prompt the user until a positive number is entered."""
    while True:
        try:
            amount = float(input(prompt))
            if amount > 0:
                return amount
            print("Amount must be greater than zero.")
        except ValueError:
            print("Invalid input! Please enter a number.")


# ---------- Core features ----------
def add_expense(category, amount, notes):
    """Append a new expense row to the CSV file."""
    df = load_data()
    new_row = pd.DataFrame([{
        "date": dt.date.today(),
        "category": category,
        "amount": amount,
        "notes": notes,
    }])
    df = pd.concat([df, new_row], ignore_index=True)
    save_data(df)


def recent_expense():
    """Return a formatted string with the latest expense."""
    df = load_data()
    if df.shape[0] == 0:
        return "No expenses have been recorded yet."

    last_row = df.iloc[-1]
    return f"""
Date:     {last_row['date']}
Category: {last_row['category']}
Amount:   {last_row['amount']}
Notes:    {last_row['notes']}
"""


def total_expenses():
    """Return a report of total spending grouped by category."""
    df = load_data()
    if df.shape[0] == 0:
        return "No expenses have been recorded yet."

    category_sum = df.groupby("category")["amount"].sum()
    message = ""
    for category, total in category_sum.items():
        message += f"{category}: {total}\n"
    message += f"Total: {df['amount'].sum()}"
    return message


# ---------- Main menu ----------
menu = """
----------
1. Add expense
2. Show latest expense
3. Show all expenses
4. Exit
"""

message = "Expense Manager\n"


# ---------- Main loop ----------
while True:
    user_input = input(message + menu).strip()

    if user_input == "1":
        category = input("Category: ").strip()
        amount = get_valid_amount()
        notes = input("Notes: ").strip()

        add_expense(category, amount, notes)
        message = f"✅ New expense added under '{category}'.\n"

    elif user_input == "2":
        message = recent_expense()

    elif user_input == "3":
        message = total_expenses()

    elif user_input == "4":
        break

    else:
        message = "⚠️ Invalid option. Please choose 1-4.\n"