# Hangman game. Guess letters in a randomly chosen word. If word is guessed correctly, you
# win. Else, you lose!

import random
from hangman_words import word_list
end_of_game = False

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Creating a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.
lives = 6
# Printing hangman logo at beginning of game
from hangman_art import logo
print (logo)
# Testing code
#print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

# Begin game
while not end_of_game:
    guess = input("Guess a letter: ").lower()
# If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You already typed {guess}")
    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #  If guess is not a letter in the chosen_word,
    # Then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop and it should print "You lose."

    if guess not in chosen_word:
        #  If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"{guess.upper()} is not in the word.You lose a life")
        lives -= 1
        #print(lives)
        if lives == 0:
            end_of_game = True
            print("You lose")
    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # printing the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    from hangman_art import stages
    print(f"Your remaining life is {lives}.{stages[lives]}")
