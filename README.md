# Personal Finance Tracker

## Overview
The **Personal Finance Tracker** is a simple, intuitive desktop application that helps users manage their personal finances by tracking income and expenses. The app uses a graphical interface built with Tkinter and stores transaction data in an SQLite database, ensuring persistence across sessions.

## Features
- **Add Transactions**: Allows users to input income or expense details, including amount, date, type, and description.
- **Transaction History**: View a comprehensive list of all transactions.
- **Financial Summary**: Displays totals for income, expenses, and current balance.
- **Data Persistence**: All transactions are saved in an SQLite database (`finance.db`) for long-term tracking.
- **User-Friendly Interface**: A simple, easy-to-navigate GUI with clear prompts and labeled fields.

## Installation
### Requirements:
- Python 3.12.3 or higher.

### Dependencies:
- No additional dependencies are required beyond the standard Python libraries (tkinter, sqlite3).

## Usage
1. **Running the Application**:
   - Run `main.py` to launch the Personal Finance Tracker application.
   
2. **Adding a Transaction**:
   - Enter the following transaction details:
     - **Amount**: The transaction amount (positive for income, negative for expenses).
     - **Type**: Choose "Income" or "Expense."
     - **Date**: Enter the transaction date in MM-DD-YYYY format.
     - **Description**: Add a brief description for the transaction.
   - Click **Add Transaction** to save the transaction.

3. **View and Manage Transactions**:
   - The transaction history is displayed in a list showing transaction ID, amount, type, date, and description.
   - Click on a transaction and press **Delete Transaction** to remove it.

4. **Check Summary**:
   - The summary section at the bottom shows:
     - **Total Income**
     - **Total Expenses**
     - **Current Balance**

## Files Included
- **main.py**: The main application file that launches the GUI and manages interactions.
- **gui.py**: Contains the `FinanceTracker` class, which creates the GUI and handles user input, transaction management, and summary updates.
- **database.py**: Handles database interactions, including:
  - Initializing the SQLite database (`init_db`)
  - Adding transactions (`add_transaction_to_db`)
  - Deleting transactions (`delete_transaction_from_db`)
  - Retrieving all transactions (`get_all_transactions`)

The database (`finance.db`) is automatically created if it doesn’t already exist, storing transaction data persistently.

## Credits
- **Programmer**: [Adelita Martinez](https://www.linkedin.com/in/adelitamartinez/)
- **Email**: 94martinez.adelita@gmail.com

## License
This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.

