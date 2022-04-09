import requests
from tkinter import *


# ----- Making the API request. API Credit: https://friends-quotes-api.herokuapp.com/-------#
def quote_request():
    """Creates the API request to the endpoint and displays the quote and author"""
    response = requests.get(url="https://friends-quotes-api.herokuapp.com/quotes/random")
    response.raise_for_status()
    quote = response.json()['quote']
    char = response.json()['character']
    total = quote + "\n" + char
    canvas.itemconfig(quote_text, text=total)


# -------------- UI Creation---------------#
window = Tk()
window.title("QUOTES FROM FRIENDS TV SHOW")
window.config(padx=50, pady=50)

# Quote background creation
canvas = Canvas(width=300, height=614)
quote_image = PhotoImage(file="background.png")
canvas.create_image(160, 207, image=quote_image)
quote_text = canvas.create_text(150, 207, text="Friends Quote goes here", font=("Arial", 24, "bold"), width=250)
canvas.grid(row=0, column=0)

# Button creation that calls quote_request function when user clicks the button.
button = Button(text="How you doin?", font=("Arial", 24, "bold"), command=quote_request)
button.grid(row=1, column=0, columnspan=4)
window.mainloop()
