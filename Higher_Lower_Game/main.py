# Higher Lower game for celebrity instagram accounts.
# Who has the most followers?


import random
from art import logo, vs
from game_data import data
from os import system, name


def clear():
    """Clears screen after user wants to restart game."""
    # for windows
    if name == 'nt':
        _ = system('cls')
        # for mac and linux
    else:
        _ = system('clear')


current_score = 0
num_followers1 = 0
num_followers2 = 0
answer = ''
# Printing game logo1
print(logo)

# Generating first random question from game_data.py
question1 = random.choice(data)
num_followers1 = question1['follower_count']
#print(num_followers1)
print(f"Compare A: {question1['name']}, a {question1['description']}, from {question1['country']}")




# Looping the game
game_continue = True
while game_continue:
    # Printing game logo2
    print(vs)

    # Generating second random question from game_data.py
    question2 = random.choice(data)

    # Avoiding same question to be repeated.
    if question1==question2:
        question2=random.choice(data)
    num_followers2 = question2['follower_count']
    # For debugging purposes
    # print(num_followers2)

    # Making a dictionary for questions 1 and 2. Need number of followers
    # And question.
    user_choice = {

        "A": [num_followers1, question1],
        "B": [num_followers2, question2],
    }
    # For debugging purposes
    # print(user_choice["A"])
    # For debugging purposes
    # print(user_choice["B"])
    # Finding max using key

    # Checking for which key has the higher number of followers.
    max_num = 0
    for high in user_choice:
        if user_choice[high][0] > max_num:
            max_num = user_choice[high][0]
            # For debugging purposes
            #print(f" max_num is {max_num}")
            getting_key = high
            question = user_choice[high][1]
    # Testing for loop
    # print(max_num, getting_key, question)
    print(f"Against B: {question2['name']}, a {question2['description']}, from {question2['country']}")

    answer = (input("Who has more followers. Type 'A' or 'B': ").upper())


    print(logo)
    if answer == getting_key:
        current_score += 1
        clear()
        print (logo)
        print(f"You are right. Current_score: {current_score}")
        question1 = user_choice["B"][1]
        num_followers1 = num_followers2
        print(f"Compare A: {question1['name']}, a {question1['description']}, from {question1['country']}")
        #print(question)

    else:
        game_continue = False
        print(f"Sorry,that's the wrong answer. Final score: {current_score}")

