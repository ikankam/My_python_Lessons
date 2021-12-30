# Password Generator Project (without for loop)
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# choosing characters
select_letters = random.choices(letters, k=nr_letters)
Char = ''.join(map(str, select_letters))

# choosing symbols
select_symbols = random.choices(symbols, k=nr_symbols)
Sym = ''.join(map(str, select_symbols))

# choosing numbers
select_numbers = random.choices(numbers, k=nr_numbers)
Num = ''.join(map(str, select_numbers))

Password = Char + Sym + Num
print(f"Your password is: {Password}")

#  Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# choosing characters
select_letters = random.choices(letters, k=nr_letters)

# choosing numbers
select_numbers = random.choices(numbers, k=nr_numbers)

# choosing symbols
select_symbols = random.choices(symbols, k=nr_symbols)

Pass_list = select_letters + select_numbers + select_symbols
# shuffling list to create randomness

random.shuffle(Pass_list)
Random_Password = ''.join(map(str, Pass_list))
print(f"Your random password is: {Random_Password}" )
