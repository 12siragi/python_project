import random

def guessing_game():
    number = random.randint(1, 100)
    guess = None
    attempts = 0

    while guess != number:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")

    print(f"Congratulations! You guessed the number {number} in {attempts} attempts.")

guessing_game()

