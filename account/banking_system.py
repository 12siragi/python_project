# banking_system.py

from account import Account
from transaction import transfer

def main():
    # Create accounts
    acc1 = Account('12345', 1000)
    acc2 = Account('67890', 500)

    # Display initial balances
    print(f"Initial Balance of Account 1: ${acc1.check_balance()}")
    print(f"Initial Balance of Account 2: ${acc2.check_balance()}")

    # Perform a transfer
    try:
        transfer(acc1, acc2, 200)
        print("Transfer successful!")
    except ValueError as e:
        print(f"Error: {e}")

    # Display final balances
    print(f"Final Balance of Account 1: ${acc1.check_balance()}")
    print(f"Final Balance of Account 2: ${acc2.check_balance()}")

if __name__ == "__main__":
    main()

