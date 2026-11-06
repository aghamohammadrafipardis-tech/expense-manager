# 💰 Expense Manager

A simple command-line expense tracker built with Python and Pandas.

## ✨ Features

- ➕ Add a new expense (category, amount, notes)
- 🕒 Show the latest recorded expense
- 📊 Show all expenses grouped by category with totals
- 💾 Persistent storage in a CSV file

## 🧰 Requirements

- 🐍 Python 3.9+
- 🐼 pandas 2.0+

## 🚀 Installation

```bash
pip install -r requirements.txt
```

## 🎮 Usage

```bash
python main.py
```

The program shows the following menu:

```text
1. Add expense
2. Show latest expense
3. Show all expenses
4. Exit
```

## 🗂️ Data Format

Expenses are stored in `expenses.csv` with these columns:

| Column   | Description              |
|----------|--------------------------|
| date     | Date of the expense      |
| category | Category of the expense  |
| amount   | Amount spent (positive)  |
| notes    | Free-text description    |

### Sample

```csv
date,category,amount,notes
2025-01-15,Food,25000,Lunch
2025-01-16,Transport,8000,Taxi
2025-01-17,Entertainment,15000,Cinema
```

A ready-to-use sample file `sample_expenses.csv` is included.

## 📜 License

MIT
