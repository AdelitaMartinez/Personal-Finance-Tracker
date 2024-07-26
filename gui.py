# gui.py
# Programmer: Adelita Martinez
# Email: amartinez1013@cnm.edu
# Purpose: Personal finance tracker application to track expenses and income
# Python Version: 3.12.3

import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime

class FinanceTracker:
  def __init__(self, root):
    self.root = root
    self.root.title("Personal Finance Tracker")

    # Create and place GUI complenets
    self.create_widgets()

    # Initialize SQLite database
    self.init_db()

  def create_widgets(self):
    # Create and place widgets

    # Amount widget
    self.amount_label = tk.Label(self.root, text="Amount")
    self.amount_label.pack()
    self.amount_entry = tk.Entry(self.root)
    self.amount_entry.pack()

    # Income and expense widget
    self.type_label = tk.Label(self.root, text="Type (income/expense)")
    self.type_label.pack()
    self.type_entry = tk.Entry(self.root)
    self.type_entry.pack()

    # Date
    self.date_label = tk.Label(self.root, text="Date (YYYY-MM-DD)")
    self.date_label.pack()
    self.date_entry = tk.Entry(self.root)
    self.date_entry.pack()

    # Description
    self.desc_label = tk.Label(self.root, text="Description")
    self.desc_label.pack()
    self.desc_entry = tk.Entry(self.root)
    self.desc_entry.pack()

    # Add buttons
    self.add_button = tk.Button(self.root, text="Add Transaction", command=self.add_transaction)
    self.add_button.pack()

    self.delete_button = tk.Button(self.root, text="Delete Transaction", command=self.delete_transaction)
    self.delete_button.pack()

    self.transactions_list = tk.Listbox(self.root)
    self.transactions_list.pack()

    self.summary_label = tk.Label(self.root, text="Summary")
    self.summary_label.pack()

  def init_db(self):
        # Initialize SQLite database
        self.conn = sqlite3.connect('finance.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS transactions
                             (id INTEGER PRIMARY KEY, amount REAL, type TEXT, date TEXT, description TEXT)''')
        self.conn.commit()

  def add_transaction(self):
        # Function to add a transaction
        amount = self.amount_entry.get()
        trans_type = self.type_entry.get()
        date = self.date_entry.get()
        description = self.desc_entry.get()

        self.cursor.execute("INSERT INTO transactions (amount, type, date, description) VALUES (?, ?, ?, ?)",
                            (amount, trans_type, date, description))
        self.conn.commit()

        self.load_transactions()

  def delete_transaction(self):
        # Function to delete a transaction
        selected = self.transactions_list.curselection()
        if selected:
            trans_id = self.transactions_list.get(selected).split()[0]
            self.cursor.execute("DELETE FROM transactions WHERE id=?", (trans_id,))
            self.conn.commit()
            self.load_transactions()
        else:
            messagebox.showwarning("Warning", "Please select a transaction to delete")

  def load_transactions(self):
        # Function to load transactions from the database
        self.transactions_list.delete(0, tk.END)
        self.cursor.execute("SELECT * FROM transactions")
        for row in self.cursor.fetchall():
            self.transactions_list.insert(tk.END, f"{row[0]} {row[1]} {row[2]} {row[3]} {row[4]}")
