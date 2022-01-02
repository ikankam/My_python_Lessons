# Caesar Cipher encryption and decryption project
# Takes input from user. Asks to encrypt or decrypt message.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# Adding logo
from art import logo
print (logo)

# Combining the encrypt() and decrypt() functions into a single function called caesar().
def caesar(message, shift_amount, choice):
    text = ""

    if choice == "encode":
        for char in message:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift_amount
                text += alphabet[new_position]
            else:
                text+= char
        print(f"The encoded text is {text}")


    elif choice == "decode":
        for char in message:
            if char in alphabet:
                position = alphabet.index(letter)
                new_position = position - shift_amount
                text += alphabet[new_position]
        else:
            text+=char
        print(f"The decoded text is {text}")


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
shift%=26
caesar(message=text, shift_amount=shift, choice=direction)

# Looping game till user types 'no' to quit game
end_game=False
while end_game!=True:
  answer=input("Would you like to go again? Type 'yes' or 'no'\n")
  if answer=='yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift %= 26
    caesar(message=text, shift_amount=shift, choice=direction)
  elif answer=='no':
    end_game=True







'''# Reorg number two
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
game_continue=True
while game_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift%=26
    caesar(message=text, shift_amount=shift, choice=direction)
    
answer=input("Would you like to go again? Type 'yes' or 'no'\n")
if answer=='no':
    game_continue=False
    

def caesar(message, shift_amount, choice):
    text = ""
    if choice == "decode":
        shift_amount *= -1
        print(shift_amount)
    for letter in message:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        # print (new_position)
        text += alphabet[new_position]
    print(f"The {choice}d text is {text}")'''


