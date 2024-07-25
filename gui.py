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

    