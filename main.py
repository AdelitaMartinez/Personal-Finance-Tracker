# main.py
# Programmer: Adelita Martinez
# Email: 94martinez.adelita@gmail.com
# Purpose: Personal finance tracker app to track expenses and income
# Python Version: 3.12.3

import tkinter as tk
from gui import FinanceTracker

if __name__ == "__main__":
  root = tk.Tk()
  app = FinanceTracker(root)
  root.mainloop()

