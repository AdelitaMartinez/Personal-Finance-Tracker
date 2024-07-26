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