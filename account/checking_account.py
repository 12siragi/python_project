from datetime import datetime
from account import Account

class CheckingAccount(Account):
    def __init__(self, account_number, balance=0, overdraft_limit=0):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance + self.overdraft_limit:
                self.balance -= amount
                self.transactions.append((datetime.now(), "Withdrawal", amount))
            else:
                raise ValueError("Insufficient funds including overdraft limit")
        else:
            raise ValueError("Withdrawal amount must be positive")
