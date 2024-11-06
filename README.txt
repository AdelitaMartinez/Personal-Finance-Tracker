Personal Finance Tracker
========================

Author: Adelita Martinez  
Contact: 94martinez.adelita@gmail.com 
Python Version: 3.12.3  

Overview
--------
The **Personal Finance Tracker** is a simple, intuitive desktop application that allows users to track income, expenses, and balances, helping them manage their personal finances effectively. The app uses a graphical interface built with Tkinter and stores transaction data in an SQLite database for easy access and reliability across sessions.

Features
--------
- **Add Transactions**: Record income or expense details, including amount, date, type, and description.
- **Transaction History**: View a comprehensive list of all transactions.
- **Financial Summary**: See totals for income, expenses, and current balance.
- **Data Persistence**: Transactions are saved in an SQLite database for easy retrieval and long-term tracking.
- **User-Friendly Interface**: Simple, labeled fields and clear prompts ensure ease of use.

Installation and Setup
----------------------
1. **Clone or Download the Project**: Save the project files to your local machine.
2. **Install Python 3.12.3**: Make sure you have Python installed. The app only requires standard libraries, so no additional packages are necessary.
3. **Run the Application**: Navigate to the project folder and start the app with the command:


Usage Instructions
------------------
1. **Launch the Application**:
- Run `main.py` to open the Personal Finance Tracker.

2. **Add a Transaction**:
- Enter transaction details in the following fields:
  - **Amount**: Transaction amount
  - **Type**: Specify if it’s an income or expense
  - **Date**: Enter date in MM-DD-YYYY format
  - **Description**: Add a brief description
- Click **Add Transaction** to save it.

3. **View and Manage Transactions**:
- View all transactions in the list, displayed with their ID, amount, type, date, and description.
- Select a transaction and click **Delete Transaction** to remove it.

4. **Check Summary**:
- The summary section at the bottom shows your total income, total expenses, and current balance.

File Structure and Details
--------------------------
- **main.py**: The main file that launches the `FinanceTracker` application by initializing the Tkinter root window and GUI.
- **gui.py**: Contains the `FinanceTracker` class, which creates the user interface, handles user interactions, and updates the summary. This file also includes methods for adding and deleting transactions and loads data from the database.
- **database.py**: Handles all database-related tasks, including:
- Initializing the SQLite database (`init_db`)
- Adding transactions (`add_transaction_to_db`)
- Deleting transactions (`delete_transaction_from_db`)
- Retrieving all transactions (`get_all_transactions`)

The database (`finance.db`) is created automatically if it doesn’t already exist, storing transaction data persistently.

Future Enhancements
-------------------
- **Data Export**: Add an option to export transactions as CSV.
- **Visual Analytics**: Display charts showing income and expense trends.
- **Advanced Filters**: Implement filters by date, type, and categories.

License
-------
This project is licensed under the Apache License 2.0 - see the LICENSE file for details.





