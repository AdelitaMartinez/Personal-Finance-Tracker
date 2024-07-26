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
        self.root.geometry("400x500")

        # Create and place GUI components
        self.create_widgets()

        # Initialize SQLite database
        self.init_db()

    def create_widgets(self):
        # Create a frame for the input fields and buttons
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)

        # Amount input
        self.amount_label = tk.Label(input_frame, text="Amount")
        self.amount_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
        self.amount_entry = tk.Entry(input_frame)
        self.amount_entry.grid(row=0, column=1, padx=5, pady=5)

        # Type input
        self.type_label = tk.Label(input_frame, text="Type (income/expense)")
        self.type_label.grid(row=1, column=0, padx=5, pady=5, sticky='e')
        self.type_entry = tk.Entry(input_frame)
        self.type_entry.grid(row=1, column=1, padx=5, pady=5)

        # Date input
        self.date_label = tk.Label(input_frame, text="Date (MM-DD-YYYY)")
        self.date_label.grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.date_entry = tk.Entry(input_frame)
        self.date_entry.grid(row=2, column=1, padx=5, pady=5)

        # Description input
        self.desc_label = tk.Label(input_frame, text="Description")
        self.desc_label.grid(row=3, column=0, padx=5, pady=5, sticky='e')
        self.desc_entry = tk.Entry(input_frame)
        self.desc_entry.grid(row=3, column=1, padx=5, pady=5)

        # Add transaction button
        self.add_button = tk.Button(input_frame, text="Add Transaction", command=self.add_transaction)
        self.add_button.grid(row=4, columnspan=2, pady=10)

        # Delete transaction button
        self.delete_button = tk.Button(input_frame, text="Delete Transaction", command=self.delete_transaction)
        self.delete_button.grid(row=5, columnspan=2, pady=5)

        # Transactions list
        self.transactions_list = tk.Listbox(self.root, height=10, width=50)
        self.transactions_list.pack(pady=10)

        # Summary label
        self.summary_label = tk.Label(self.root, text="Summary")
        self.summary_label.pack(pady=10)

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
        date_str = self.date_entry.get()
        description = self.desc_entry.get()

        # Convert the date format from MM-DD-YYYY to YYYY-MM-DD
        try:
            date_obj = datetime.strptime(date_str, "%m-%d-%Y")
            date = date_obj.strftime("%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Invalid Date", "Date must be in MM-DD-YYYY format")
            return

        self.cursor.execute("INSERT INTO transactions (amount, type, date, description) VALUES (?, ?, ?, ?)",
                            (amount, trans_type, date, description))
        self.conn.commit()

        self.load_transactions()
        self.update_summary()

    def delete_transaction(self):
        # Function to delete a transaction
        selected = self.transactions_list.curselection()
        if selected:
            trans_id = self.transactions_list.get(selected).split()[0]
            self.cursor.execute("DELETE FROM transactions WHERE id=?", (trans_id,))
            self.conn.commit()
            self.load_transactions()
            self.update_summary()
        else:
            messagebox.showwarning("Warning", "Please select a transaction to delete")

    def load_transactions(self):
        # Function to load transactions from the database
        self.transactions_list.delete(0, tk.END)
        self.cursor.execute("SELECT * FROM transactions")
        for row in self.cursor.fetchall():
            self.transactions_list.insert(tk.END, f"{row[0]} {row[1]} {row[2]} {row[3]} {row[4]}")

    def update_summary(self):
        # Function to update total income, expenses, and balance
        self.cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='income'")
        total_income = self.cursor.fetchone()[0] or 0

        self.cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='expense'")
        total_expenses = self.cursor.fetchone()[0] or 0

        balance = total_income - total_expenses

        # Format amounts to 2 decimal places
        total_income = "{:.2f}".format(total_income)
        total_expenses = "{:.2f}".format(total_expenses)
        balance = "{:.2f}".format(balance)

        self.summary_label.config(text=f"Total Income: {total_income} | Total Expenses: {total_expenses} | Balance: {balance}")

    def save_to_db(self):
        # Function to save transactions to the database
        pass

    def load_from_db(self):
        # Function to load transactions from the database
        pass
