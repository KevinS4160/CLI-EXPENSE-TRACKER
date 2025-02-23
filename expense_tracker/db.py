# expense_tracker/db.py
import sqlite3
import os
from datetime import datetime

DB_FILE = "expenses.db"

def get_connection():
    return sqlite3.connect(DB_FILE)

def init_db():
    if not os.path.exists(DB_FILE):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                description TEXT,
                date TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

def add_expense(amount, category, description):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO expenses (amount, category, description, date)
        VALUES (?, ?, ?, ?)
    ''', (amount, category, description, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

def list_expenses():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, amount, category, description, date FROM expenses ORDER BY date DESC')
    rows = cursor.fetchall()
    conn.close()
    expenses = []
    for row in rows:
        expenses.append({
            "id": row[0],
            "amount": row[1],
            "category": row[2],
            "description": row[3],
            "date": row[4]
        })
    return expenses
