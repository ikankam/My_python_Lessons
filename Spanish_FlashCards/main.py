import random
from tkinter import *
import pandas

# -----------------------Reading CSV -----------------------------------#
data_dict = {}
try:
    data = pandas.read_csv("data/Need to learn.csv")
except:
    original_data = pandas.read_csv("data/Spanish Flashcards - Sheet1.csv")
    data_dict = original_data.to_dict(orient='records')
else:
    data_dict = data.to_dict(orient='records')

# -----------------------Choosing random words and setting timer---------------------------#
current_word = {}


def get_word():
    """Randomly selects a word from the dictionary and writes it on
    the canvas. Waits 3 secs and flips card"""
    global current_word, timer
    # Timer cancels after button is pressed
    window.after_cancel(timer)
    current_word = random.choice(data_dict)
    new_spa_word = current_word['Spanish']
    canvas.itemconfig(canvas_image, image=spanish_image)
    canvas.itemconfig(language_label, text="Spanish", fill="black")
    canvas.itemconfig(new_card, text=new_spa_word, fill="black")
    # Calling flip card after 3 seconds
    timer = window.after(3000, func=flip_card)


def flip_card():
    """Sets up English version of the flashcard and reveals it"""
    new_eng_word = current_word['English']
    canvas.itemconfig(canvas_image, image=english_image)
    canvas.itemconfig(language_label, text="English", fill="white")
    canvas.itemconfig(new_card, text=new_eng_word, fill="white")


def known_word():
    """Removes words user confirms as known and creates/updates a csv file"""
    data_dict.remove(current_word)
    to_learn = pandas.DataFrame(data_dict)
    to_learn.to_csv("data/Need to learn.csv", index=False)
    get_word()


# -------------------------------------UI SETUP------------------------------------#
BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Spanish FlashCards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# Setting 3 secs timer for card to flip to reveal english answer
timer = window.after(3000, func=flip_card)

# Flash Card Image setup
canvas = Canvas(width=800, height=526)
spanish_image = PhotoImage(file="images/card_front.png")
english_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=spanish_image)
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

# Canvas Labels
language_label = canvas.create_text(400, 150, text="Spanish", font=("Arial", 40, "italic"))
new_card = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))

# Buttons
red_button_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=red_button_image, highlightthickness=0, command=get_word)
wrong_button.grid(row=1, column=0)

green_button_image = PhotoImage(file="images/right.png")
right_button = Button(image=green_button_image, highlightthickness=0, command=known_word)
right_button.grid(row=1, column=1)

get_word()
window.mainloop()
