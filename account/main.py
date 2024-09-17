import datetime
from interest import apply_compound_interest

class Account:
    def __init__(self, balance, interest_rate, creation_date):
        self.balance = balance
        self.interest_rate = interest_rate
        self.creation_date = creation_date

def main():
    acc2 = Account(1000, 0.05, datetime.datetime(2023, 1, 1))  # Example account setup
    interest = apply_compound_interest(acc2, acc2.interest_rate)
    print(f"Calculated interest: {interest}")

if __name__ == "__main__":
    main()

