##                                                            Python Banking System
#Overview
This is a modular Python project that simulates a banking system. It includes features for account management, transactions, bill payments, user authentication, and persistence through JSON storage. The system is designed with both checking and savings accounts, and it provides a command-line interface (CLI) for interaction.

## Features
User Authentication: Users can register and log in with a username and password, securely hashed using SHA-256.
Account Types: The system supports both Checking and Savings accounts.
Transactions: Users can perform deposits, withdrawals, and view their balance.
Automated Bill Payments: Users can pay bills automatically from their accounts.
Interest Calculation: Savings accounts automatically accrue interest.
Data Persistence: Account and transaction data is stored in JSON files for persistence.
Error Handling and Validation: Ensures valid inputs and smooth error recovery.
Unit Tests: Tests are provided to validate core functionalities.

## Directory Structure
├── 100.json                   # Example account data
├── account.py                 # Base account logic
├── auth.py                    # User authentication
├── banking_system.py          # Main banking system logic
├── bill_payment.py            # Handles bill payments
├── checking_account.py        # Checking account implementation
├── cli.py                     # Command-line interface (CLI) for the system
├── coverage.py                # For code coverage testing
├── interest.py                # Interest calculation logic
├── main.py                    # Main entry point for running the system
├── persistence.py             # Handles persistence using JSON
├── savings_account.py         # Savings account implementation
├── test_account.py            # Unit tests for accounts
├── test_banking_system.py     # Unit tests for the banking system
├── transaction.py             # Transaction logic
├── users.json                 # User data

Usage
The system provides a simple CLI interface for interacting with bank accounts. To start, register or log in using your credentials:

Example Workflow:
Deposit funds:

bash
Copy code
Choose a transaction action: [deposit, withdraw, view, exit]: deposit
Enter deposit amount: 1000
Deposit successful! Your new balance is $1000.
Withdraw funds:

bash
Copy code
Choose a transaction action: [deposit, withdraw, view, exit]: withdraw
Enter withdrawal amount: 200
Withdrawal successful! Your new balance is $800.
View balance:

bash
Copy code
Choose a transaction action: [deposit, withdraw, view, exit]: view
Your current balance is $800.
Automated Bill Payment:

bash
Copy code
Schedule a bill payment: Enter amount: 100
Bill payment successful! Your remaining balance is $700.
