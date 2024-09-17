import json
from datetime import datetime

def save_account(account):
    filename = f"{account.account_number}.json"
    data = {
        'balance': account.check_balance(),
        'transactions': [(date.isoformat(), type, amount) for date, type, amount in account.transactions]
    }
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_account(account_number, account_class):
    filename = f"{account_number}.json"
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            account = account_class(account_number, data['balance'])
            account.transactions = [(datetime.fromisoformat(date), type, amount) for date, type, amount in data['transactions']]
            return account
    except FileNotFoundError:
        raise ValueError("Account not found")

