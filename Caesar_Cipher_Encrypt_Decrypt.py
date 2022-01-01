alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt (user_text, shift_amount):
  encoded_text = ""
  for letter in user_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    encoded_text += alphabet[new_position]
  print(f"The encoded text is {encoded_text}")

# Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt (user_text, shift_amount):
  decoded_text = ""
  for letter in user_text:
    position=alphabet.index(letter)
    new_position = position - shift_amount
    decoded_text+=alphabet[new_position]
  print(f"The decoded text is {decoded_text}")


# Check if the user wanted to encrypt or decrypt.
if direction =="encode":
  encrypt(user_text=text, shift_amount=shift)
elif direction=="decode":
  decrypt(user_text=text, shift_amount=shift)
else:
  print("Enter a valid prompt")
