# Simple BlackJack game
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Below  list is the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

import random
from os import system, name
from BlackJack_art import logo


def clear():
    """Clears screen after user wants to restart game."""
    # for windows
    if name == 'nt':
        _ = system('cls')
        # for mac and linux
    else:
        _ = system('clear')


def deal_card():
    """Returns a random card from the list of cards"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Takes a list of dealt cards and returns a score"""
    if len(cards) == 2 and sum(cards) == 21:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, pc_score):
    """Takes user and computer scores and compares to determine winner/outcome."""
    if user_score == pc_score:
        print("It's a draw.You and computer have the same score")
    elif pc_score == 0:
        print("Computer has a BlackJack. You lose.")
    elif user_score == 0:
        print("You have a BlackJack. You win!")
    elif user_score > 21:
        print(f"Your score {user_score} is greater than 21. You lose.")
    elif pc_score > 21:
        print(f"Computer's score {pc_score} is greater than 21. You win!")
    elif user_score > pc_score:
        print(f"You scored {user_score} which is higher than computer's score of {pc_score}.You win!")
    else:
        print("You lose.")


def play_game():
    """Function that runs the game."""
    # Creates empty lists for user and computer
    user_cards = []
    computer_cards = []
    game_over = False

    # Deals 2 random cards to both the user and the computer.

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Calls the calculate_score and tells user their hand (first two cards) and
    # reveals computer's first card only.
    # If user or computer scores a BlackJack (ie: 0) game ends. If user score over 21,
    # game ends.
    # Else, it then asks user if they want another card based on their current hand.
    # If user accepts, another card is dealt. Else, user side ends.
    while not game_over:
        user_score = calculate_score(user_cards)
        pc_score = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")
        if user_score == 0 or pc_score == 0 or user_score > 21:
            game_over = True
        else:
            user_new_card = input("Would you like to draw another card? Enter 'y' for yes and 'n' for no\n")
            if user_new_card == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    # Computer turn to play after user enters 'n' for no.
    # As long as computer score is not a BlackJack and is below 17,
    # Computer draws a card and new score is calculated.
    # When condition is met and computer is done, the compare function is called.

    while pc_score != 0 and pc_score < 17:
        computer_cards.append(deal_card())
        pc_score = calculate_score(computer_cards)
    print(f"   Computer's final cards are: {computer_cards}, computer score: {pc_score}")

    compare(user_score, pc_score)


# Getting game started
game_begin = True

while game_begin:
    start_game = input('Would you like to play BlackJack? Enter "y" for yes and "n" for no.\n')
    if start_game == 'y':
        clear()
        print(logo)
        play_game()
    elif start_game == 'n':
        game_begin = False
