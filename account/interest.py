import datetime

def apply_compound_interest(account, periods_per_year=12):
    periods = (datetime.datetime.now() - account.creation_date).days // (365 // periods_per_year)
    interest = account.balance * (1 + account.interest_rate / periods_per_year) ** periods - account.balance
    return interest

