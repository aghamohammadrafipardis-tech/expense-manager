# Expense Manager

A simple command-line expense tracker written in Python using Pandas.

## Features

- Add a new expense (category, amount, notes)
- Show the latest recorded expense
- Show all expenses grouped by category with totals
- Persistent storage in a CSV file

## Requirements

- Python 3.9+
- pandas

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

Follow the on-screen menu:

```
1. Add expense
2. Show latest expense
3. Show all expenses
4. Exit
```

## Data format

`expenses.csv` has the following columns:

| Column   | Description              |
|----------|--------------------------|
| date     | Date of the expense      |
| category | Category of the expense  |
| amount   | Amount spent (positive)  |
| notes    | Free-text description    |

## License

MIT