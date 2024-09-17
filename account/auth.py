import hashlib
import json

users_file = 'users.json'

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password):
    try:
        with open(users_file, 'r') as file:
            users = json.load(file)
    except FileNotFoundError:
        users = {}

    if username in users:
        raise ValueError("Username already exists")

    users[username] = hash_password(password)
    with open(users_file, 'w') as file:
        json.dump(users, file)

def authenticate_user(username, password):
    try:
        with open(users_file, 'r') as file:
            users = json.load(file)
    except FileNotFoundError:
        raise ValueError("No users registered")

    hashed_password = hash_password(password)
    return users.get(username) == hashed_password
