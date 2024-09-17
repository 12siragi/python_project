# test_account.py

from account import Account

def test_account_creation():
    """Test account creation and initial balance."""
    acc = Account('12345', 1000)
    assert acc.account_number == '12345', "Account number should be '12345'"
    assert acc.check_balance() == 1000, "Initial balance should be 1000"

def test_deposit():
    """Test deposit method."""
    acc = Account('12345', 1000)
    acc.deposit(500)
    assert acc.check_balance() == 1500, "Balance should be 1500 after depositing 500"

    try:
        acc.deposit(-100)
        print("Failed: Negative deposit amount should raise ValueError")
    except ValueError:
        print("Passed: Negative deposit amount raises ValueError")

def test_withdraw():
    """Test withdraw method."""
    acc = Account('12345', 1000)
    acc.withdraw(300)
    assert acc.check_balance() == 700, "Balance should be 700 after withdrawing 300"

    try:
        acc.withdraw(800)
        print("Failed: Withdrawal exceeding balance should raise ValueError")
    except ValueError:
        print("Passed: Withdrawal exceeding balance raises ValueError")

    try:
        acc.withdraw(-100)
        print("Failed: Negative withdrawal amount should raise ValueError")
    except ValueError:
        print("Passed: Negative withdrawal amount raises ValueError")

def main():
    test_account_creation()
    test_deposit()
    test_withdraw()
    print("All tests completed!")

if __name__ == "__main__":
    main()
