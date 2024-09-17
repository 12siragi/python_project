import unittest
import os
from auth import register_user, authenticate_user
from checking_account import CheckingAccount
from savings_account import SavingsAccount
from bill_payment import BillPayment
from persistence import save_account, load_account
from datetime import datetime

class TestBankingSystem(unittest.TestCase):

    def setUp(self):
        # Clear the users file to avoid "Username already exists" error
        if os.path.exists('users.json'):
            os.remove('users.json')

        # Register a user for authentication tests
        try:
            register_user("testuser", "password123")
        except ValueError:
            # User already exists, continue with the test
            pass

        self.checking_acc = CheckingAccount(account_number="CHK123456", balance=1000, overdraft_limit=500)
        self.savings_acc = SavingsAccount(account_number="SAV123456", balance=2000, interest_rate=0.05)

    def test_authentication(self):
        self.assertTrue(authenticate_user("testuser", "password123"))

    def test_bill_payment(self):
        bill = BillPayment(self.checking_acc, 200, datetime.now().date())
        bill.process_payment()
        self.assertEqual(self.checking_acc.check_balance(), 800)

    def test_persistence(self):
        save_account(self.checking_acc)
        loaded_acc = load_account("CHK123456", CheckingAccount)
        self.assertEqual(loaded_acc.check_balance(), 1000)

if __name__ == "__main__":
    unittest.main()

