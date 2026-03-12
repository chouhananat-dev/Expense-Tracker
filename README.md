# 💰 Django Expense Tracker & Analytics Dashboard

A full-stack Django application designed to help users track their daily expenses, visualize spending habits through interactive charts, and export financial data for external analysis.

## 🚀 Features

- **User Authentication:** Secure Signup, Login, and Logout functionality.
- **Expense Management (CRUD):** Users can Create, Read, Update, and Delete their own expenses.
- **Smart Filtering:** Sort and view expenses by specific Month and Year.
- **Analytical Dashboard:** - Real-time calculation of total spending.
  - Interactive **Doughnut Charts** (via Chart.js) showing spending breakdown by category.
- **Data Export:** Export filtered or full expense lists directly to **CSV (Excel compatible)**.
- **Responsive Design:** Styled with **Tailwind CSS** for a modern look on mobile and desktop.

## 🛠️ Tech Stack

- **Backend:** Python / Django
- **Frontend:** Tailwind CSS, JavaScript (Chart.js)
- **Database:** SQLite (Default)
- **File Export:** Python CSV Module

## 📦 Installation & Setup

1. **Clone the repository:**
git clone [https://github.com/chouhananat-dev/Expense-Tracker.git](https://github.com/chouhananat-dev/Expense-Tracker.git)
cd Expense-Tracker

2. **Create a virtual environment:**
   python -m venv venv
    venv\Scripts\activate

3. **Install dependencies**
    Make sure you have django installed
    python install django

4. **Run migrations**
    python manage.py migrate

5. **Run Server**
    python manage.py runserver

## 📊 Usage:
    Adding Expenses: Click the '+' button to record a new transaction.

    Filtering: Use the dropdowns at the bottom to isolate spending for a specific month.

    Analytics: Once filtered, the dashboard will generate a category-wise chart and a specific total for that period.

    Excel: Use the "Download CSV" button within the filtered results to save your data.

## ⚖️ License

Distributed under the MIT License. See `LICENSE` for more information.
