# 💸 Student Expense Tracker

A lightweight, modular Python application built to help students record daily expenses, organize spending by category, persist records locally in JSON format, and monitor monthly budget limits through both a **Command-Line Interface (CLI)** and a **Desktop Graphical User Interface (GUI)**.

🔗 **Repository Link:** [divyandiv/Expense_tracker_SEC](https://github.com)

---

## 🎯 Project Objectives

* **Track Daily Spending:** Allow students to quickly log expenses with amounts and categories (*Food, Books, Travel, Stationery, Entertainment, Other*).
* **Persistent Data Storage:** Automatically save and load expense records using a local JSON file (`expenses.json`) so data is preserved across sessions.
* **Budget Awareness:** Calculate cumulative expenses in real time and trigger an alert whenever monthly spending exceeds the **Rs. 5,000** threshold.
* **Collaborative Git Workflow:** Demonstrate industry-standard version control practices including feature branching, Pull Requests, peer code reviews, and merge conflict resolution.

---

## 👥 Team Members & Contributions

| Role | Full Name | Roll No. | Branch | Key Contributions |
| :--- | :--- | :---: | :--- | :--- |
| **Student 1 (Owner)** | **Anuradha Singh** | `14` | `feature-anuradha` | Repository setup, JSON persistence (`storage.py`: save, load, delete functions), CLI menu integration (`main.py`), and PR merge. |
| **Student 2 (Collaborator)** | **Anshika Ganjoo** | `13` | `feature-member2` | Expense analytics (`analytics.py`: total calculator, category filter, monthly budget warning alert), CLI integration, and merge conflict resolution. |

---

## ✨ Features & Technologies

### Core Features
* **Add & Delete Expenses:** Record new transactions or remove entries by index/row selection.
* **Category Filtering:** Filter expenses dynamically by category (*case-insensitive*).
* **Monthly Budget Warning Alert:** Displays live spending status, remaining balance, and an instant warning banner if spending crosses **Rs. 5,000**.
* **Dual Interface Support:** Run either the classic terminal CLI (`main.py`) or the modern card-based Tkinter desktop dashboard (`gui.py`).

### Technologies Used
* **Language:** Python 3.x
* **Data Persistence:** Python `json` module (`expenses.json`)
* **Desktop UI:** Python `tkinter` & `ttk` (zero external dependencies required)
* **Version Control:** Git & GitHub

---

## 📂 Project Structure

```text
Expense_tracker_SEC/
├── main.py            # Command-Line Interface (CLI) entry point
├── gui.py             # Tkinter Desktop Graphical User Interface (GUI)
├── storage.py         # JSON file save, load, and delete operations
├── analytics.py       # Total calculation, category filter, and budget alerts
├── expenses.json      # Local JSON database (auto-generated on first save)
├── CONTRIBUTING.md    # Guidelines for team collaboration and Git workflow
├── .gitignore         # Ignored cache and temporary files
└── README.md          # Project documentation
```

---

## ⚙️ Installation & Execution Instructions

### 1. Prerequisites
Ensure **Python 3.8+** is installed on your machine. You can verify your installation by running:
```bash
python --version
```
*(No external third-party libraries are required; `json` and `tkinter` come built into standard Python).*

### 2. Clone the Repository
Open **Git Bash** or your terminal and clone the project:
```bash
git clone https://github.com.git
cd Expense_tracker_SEC
```

### 3. Run the Application
* **Option A — Launch the Desktop GUI (Recommended):**
  ```bash
  python gui.py
  ```
* **Option B — Launch the Terminal CLI:**
  ```bash
  python main.py
  ```

---

## 🖥️ Sample Output
