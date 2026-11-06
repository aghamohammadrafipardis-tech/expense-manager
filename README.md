<div align="center">

# 💰 Expense Manager

### A simple, elegant command-line expense tracker built with Python & Pandas

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)]()

---

**Track your daily expenses from the terminal — fast, simple, and persistent.**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Data Format](#-data-format) • [License](#-license)

</div>

---

## ✨ Features

| | Feature | Description |
|---|---|---|
| ➕ | **Add expense** | Record a new expense with category, amount, and notes |
| 🕒 | **Latest expense** | Instantly view the most recently recorded expense |
| 📊 | **Category report** | See all expenses grouped by category with totals |
| 💾 | **Persistent storage** | All data is safely stored in a CSV file |

---

## 🧰 Requirements

| Tool | Version |
|---|---|
| 🐍 Python | 3.9 or higher |
| 🐼 pandas | 2.0 or higher |

---

## 🚀 Installation

```bash
# 1. Clone the repository
git clone https://github.com/aghamohammadrafipardis-tech/expense-manager.git

# 2. Move into the project folder
cd expense-manager

# 3. (Optional) Create a virtual environment
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS / Linux:
source .venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt
```

---

## 🎮 Usage

```bash
python main.py
```

You will see the following menu:

```text
----------
1. Add expense
2. Show latest expense
3. Show all expenses
4. Exit
```

### 📝 Example session

```text
Expense Manager
----------
1. Add expense
2. Show latest expense
3. Show all expenses
4. Exit
> 1
Category: Food
Amount: 25000
Notes: Lunch with colleagues

✅ New expense added under 'Food'.

----------
1. Add expense
2. Show latest expense
3. Show all expenses
4. Exit
> 3
Food: 55000.0
Transport: 13000.0
Total: 68000.0
```

---

## 🗂️ Data Format

Expenses are stored in `expenses.csv` with the following columns:

| 📅 Column | 📖 Description |
|---|---|
| `date` | Date of the expense (`YYYY-MM-DD`) |
| `category` | Category of the expense (e.g., Food, Transport) |
| `amount` | Amount spent (must be positive) |
| `notes` | Free-text description |

### 📄 Sample

```csv
date,category,amount,notes
2025-01-15,Food,25000,Lunch
2025-01-16,Transport,8000,Taxi
2025-01-17,Entertainment,15000,Cinema
```

> 🎁 A ready-to-use sample file is included: **`sample_expenses.csv`**.  
> To try it, copy it to `expenses.csv`:
>
> ```bash
> cp sample_expenses.csv expenses.csv   # macOS / Linux
> copy sample_expenses.csv expenses.csv # Windows (PowerShell)
> ```

---

## 📁 Project Structure

```text
expense-manager/
├── 📄 main.py               # Main program
├── 📄 requirements.txt      # Dependencies
├── 📄 README.md             # Project documentation
├── 📄 .gitignore            # Files ignored by Git
├── 📄 LICENSE               # MIT License
└── 📄 sample_expenses.csv   # Sample data for testing
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. 🍴 Fork the project
2. 🌿 Create your feature branch: `git checkout -b feature/amazing-feature`
3. ✅ Commit your changes: `git commit -m "feat: add amazing feature"`
4. 📤 Push to the branch: `git push origin feature/amazing-feature`
5. 🔃 Open a Pull Request

---

## 📜 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for more information.

---

<div align="center">

### ⭐ If you find this project useful, please give it a star!

Made with ❤️ and ☕ by [Agha Mohammad Rafi Pardis](https://github.com/aghamohammadrafipardis-tech)

</div>
