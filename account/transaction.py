from datetime import datetime

def record_transaction(account, transaction_type, amount, currency):
    """Records a transaction for the given account."""
    if transaction_type in ['Deposit', 'Withdrawal', 'Fee', 'Interest']:
        if amount > 0:
            account.transactions.append((datetime.now(), transaction_type, amount, currency))
        else:
            raise ValueError(f"{transaction_type} amount must be positive")
    else:
        raise ValueError("Invalid transaction type")

