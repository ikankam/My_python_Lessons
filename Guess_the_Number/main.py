# Guess the number game. User is made to guess
# a pc generated number.
# User is allowed to choose between easy (10 attempts)
# and hard (5 attempts) levels.
# Feedback is given based on whether user is right or wrong. 
import random
from art import logo

# Printing game logo
print(logo)

# Setting game constants (easy level gives 10) attempts
# and (hard level gives 5) and welcoming the user.

EASY_LEVEL = 10
HARD_LEVEL = 5
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# PC choosing a random number from 1 to 100
pc_guess = random.randint(1, 100)
# Printing guess for easy debugging
# print(pc_guess)

user_guess = 0
attempts = 0


def check_answer(user_guess, pc_guess, attempts):
    """Takes user_guess, pc_guess and attempts.
    Compares user_guess and pc_guess to determine
    if user is right or wrong. Reduces attempts by
    1 with each wrong answer. """
    if user_guess > pc_guess:
        print("Too high")
        return attempts - 1
    elif user_guess < pc_guess:
        print("Too low")
        return attempts - 1
    elif user_guess == pc_guess:
        print(f"You guessed right. The answer is {user_guess}")

def game():
    global user_guess
    # Allows user to input level of difficulty
    level = input("Choose a difficulty. Type 'easy' or 'hard':")
    if level == 'easy':
        attempts = EASY_LEVEL
    elif level == 'hard':
        attempts = HARD_LEVEL

    while user_guess != pc_guess:
        print(f"You have {attempts} attempts remaining.")
        user_guess = int(input("Make a guess:"))
        result = check_answer(user_guess, pc_guess, attempts)
        attempts = result
        if attempts == 0:
            print(f"You could not guess my number correctly. You lose. :( \nAnswer was {pc_guess}")
            return


game()
