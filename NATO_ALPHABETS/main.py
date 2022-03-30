from tkinter import *
from tkinter import messagebox

import pandas

# ------------NATO ALPHABET GENERATOR--------#
# Reading from csv file
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)
#  Creating a dictionary in this format:
alphabets = {value.letter: value.code for (row, value) in data.iterrows()}
# {"A": "Alfa", "B": "Bravo"}format

#print(alphabets)


# Creating a list of the phonetic code words from a word that the user inputs and catch exceptions
def generate_phonetic():
    try:
        result_entry.delete(0,'end')
        user_input = name_entry.get().upper()
        Nato = [alphabets[letter] for letter in user_input]
        ella = str(Nato)
        result_entry.insert(0, ella)
    except KeyError:
        messagebox.showerror(title="UH OH!", message="Please name/word should be letters only with no spaces.")


# ----------- UI SETUP-------------- #
window = Tk()
window.title("NATO ALPHABETS FOR PHONE CALLS")
window.config(padx=50, pady=50)

# canvas = Canvas(width=200, height=200)
# phone_img = PhotoImage(file="small-telephone-icon-9.jpg")
# canvas.create_image(100, 100, image=phone_img)
# canvas.grid(column=1, row=0)

# Labels
name_label = Label(text="Name/Word:")
name_label.grid(column=0, row=1)

# Labels
nato_result = Label(text="NATO alphabet result:")
nato_result.grid(column=0, row=2)

# Entries
name_entry = Entry(width=100)
name_entry.grid(column=1, row=1)
name_entry.focus()

result_entry = Entry(width=100)
result_entry.grid(column=1, row=2)
result_entry.focus()

# Buttons
result_button = Button(text="Generate Result", command=generate_phonetic)
result_button.grid(column=1, row=3)

window.mainloop()
