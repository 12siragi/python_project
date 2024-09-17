from datetime import datetime

class Account:
    def __init__(self, account_number, balance=0, currency='USD'):
        self.account_number = account_number
        self.balance = balance
        self.currency = currency
        self.transactions = []
        self.creation_date = datetime.now()
        self.transaction_limit = 10000  # Default daily limit in USD

    def deposit(self, amount):
        """Deposits money into the account."""
        if amount > 0:
            if self._check_daily_limit(amount, 'Deposit'):
                self.balance += amount
                self.transactions.append((datetime.now(), "Deposit", amount, self.currency))
            else:
                raise ValueError("Deposit amount exceeds daily limit")
        else:
            raise ValueError("Deposit amount must be positive")

    def withdraw(self, amount):
        """Withdraws money from the account."""
        if amount > 0:
            if amount <= self.balance:
                if self._check_daily_limit(amount, 'Withdrawal'):
                    self.balance -= amount
                    self.transactions.append((datetime.now(), "Withdrawal", amount, self.currency))
                else:
                    raise ValueError("Withdrawal amount exceeds daily limit")
            else:
                raise ValueError("Insufficient funds")
        else:
            raise ValueError("Withdrawal amount must be positive")

    def check_balance(self):
        """Returns the current balance of the account."""
        return self.balance

    def view_transactions(self):
        """Returns a formatted list of transactions."""
        return [f"{date}: {type} {amount} {currency}" for date, type, amount, currency in self.transactions]

    def _check_daily_limit(self, amount, transaction_type):
        """Checks if the transaction amount exceeds the daily limit."""
        today = datetime.now().date()
        daily_transactions = [txn for txn in self.transactions if txn[0].date() == today and txn[1] == transaction_type]
        daily_total = sum(txn[2] for txn in daily_transactions)
        return daily_total + amount <= self.transaction_limit
