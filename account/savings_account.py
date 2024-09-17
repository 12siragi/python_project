from account import Account
from datetime import datetime

class SavingsAccount(Account):
    def __init__(self, account_number, balance=0, interest_rate=0.01, currency='USD'):
        super().__init__(account_number, balance, currency)
        self.interest_rate = interest_rate
        self.transaction_limit = 10000  # Lower limit for savings accounts

    def apply_interest(self):
        """Calculates and adds interest to the account balance."""
        interest = self.balance * self.interest_rate
        self.balance += interest
        self.transactions.append((datetime.now(), "Interest", interest, self.currency))

    def apply_compound_interest(self, periods_per_year=12):
        """Applies compound interest."""
        periods = (datetime.now() - self.creation_date).days // (365 // periods_per_year)
        if periods > 0:
            for _ in range(periods):
                self.apply_interest()
                self.creation_date = datetime.now()
