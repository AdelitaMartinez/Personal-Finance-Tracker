# gui.py
# Programmer: Adelita Martinez
# Email: amartinez1013@cnm.edu
# Purpose: Create database
# Python Version: 3.12.3

import sqlite3

def init_db():
    # Initialize SQLite database
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS transactions
                      (id INTEGER PRIMARY KEY, amount REAL, type TEXT, date TEXT, description TEXT)''')
    conn.commit()
    conn.close()

def add_transaction_to_db(transaction):
    # Function to add a transaction to the database
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO transactions (amount, type, date, description) VALUES (?, ?, ?, ?)",
                   (transaction['amount'], transaction['type'], transaction['date'], transaction['description']))
    conn.commit()
    conn.close()

def delete_transaction_from_db(transaction_id):
    # Function to delete a transaction from the database
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM transactions WHERE id=?", (transaction_id,))
    conn.commit()
    conn.close()

def get_all_transactions():
    # Function to get all transactions from the database
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions")
    transactions = cursor.fetchall()
    conn.close()
    return transactions