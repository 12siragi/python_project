from datetime import datetime

class BillPayment:
    def __init__(self, account, amount, date):
        self.account = account
        self.amount = amount
        self.date = date

    def process_payment(self):
        if self.amount > 0 and self.amount <= self.account.check_balance():
            self.account.withdraw(self.amount)
            self.account.transactions.append((self.date, "Bill Payment", self.amount))
            return True
        return False
