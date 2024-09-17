from checking_account import CheckingAccount
from savings_account import SavingsAccount
from auth import register_user, authenticate_user
from bill_payment import BillPayment
from persistence import save_account, load_account

def main():
    while True:
        action = input("Choose an action: [register, login, exit]: ").strip().lower()
        
        if action == "register":
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            try:
                register_user(username, password)
                print("User registered successfully")
            except ValueError as e:
                print(e)

        elif action == "login":
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            try:
                authenticate_user(username, password)
                print("Login successful")
                while True:
                    account_action = input("Choose an account action: [create, load, exit]: ").strip().lower()
                    
                    if account_action == "create":
                        acc_type = input("Enter account type [checking, savings]: ").strip().lower()
                        account_number = input("Enter account number: ").strip()
                        if acc_type == "checking":
                            account = CheckingAccount(account_number)
                        elif acc_type == "savings":
                            account = SavingsAccount(account_number)
                        else:
                            print("Invalid account type")
                            continue
                        save_account(account)
                        print(f"{acc_type.capitalize()} account created and saved")

                    elif account_action == "load":
                        account_number = input("Enter account number to load: ").strip()
                        try:
                            account = load_account(account_number, CheckingAccount)
                            print("Account loaded successfully")
                            while True:
                                transaction_action = input("Choose a transaction action: [deposit, withdraw, view, exit]: ").strip().lower()
                                
                                if transaction_action == "deposit":
                                    amount = float(input("Enter deposit amount: ").strip())
                                    try:
                                        account.deposit(amount)
                                        save_account(account)
                                    except ValueError as e:
                                        print(e)

                                elif transaction_action == "withdraw":
                                    amount = float(input("Enter withdrawal amount: ").strip())
                                    try:
                                        account.withdraw(amount)
                                        save_account(account)
                                    except ValueError as e:
                                        print(e)

                                elif transaction_action == "view":
                                    print(account.view_transactions())

                                elif transaction_action == "exit":
                                    break

                                else:
                                    print("Invalid action")

                        except ValueError as e:
                            print(e)

                    elif account_action == "exit":
                        break

                    else:
                        print("Invalid action")

            except ValueError as e:
                print(e)

        elif action == "exit":
            break

        else:
            print("Invalid action")

if __name__ == "__main__":
    main()

