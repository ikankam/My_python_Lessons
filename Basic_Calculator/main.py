# Calculator

# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


# Exponent or power of
def exponent(n1, n2):
    return n1 ** n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": exponent,
}

from calc_art import logo
print (logo)


def calculator():
    calc_continue = True
    num1 = float(input("Enter first number:"))
    while calc_continue:
        for symbol in operations:
            print(symbol)
        user_symbol = input("Choose an operation from list above\n")
        num2 = float(input("Enter next number:"))

        Calculate = operations[user_symbol]
        answer = Calculate(num1, num2)
        print(f"{num1} {user_symbol} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer} or 'n' to start a new calculation:\n") == 'y':
            num1 = answer
        else:
            calc_continue = False
            calculator()


calculator()
