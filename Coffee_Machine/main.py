# Virtual coffee machine. User inputs choice of coffee (espresso, latte, capuccino)
# if there are enough resources to make the selected coffee, you insert your coins (quarters, nickels,
# pennies and dimes). If there is insufficient resources, user will get feedback and drink is not dispensed.
# If money inserted is enough/more than the drink requested, the drink is dispensed and change is given.
# If the money inserted is not enough, money is returned with feedback to let user know.
# User can check available resources before-hand by typing "report".
# To turn the coffee machine off, user inputs "off"
#


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

money = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(order_ingredients):
    """Checks to see if available ingredients are sufficient to make the order. Returns True if
    sufficient and returns false if insufficient"""
    is_sufficient = True
    for ingredient in order_ingredients:
        if order_ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry. There is not enough {ingredient}")
            is_sufficient = False
    return is_sufficient


# TODO 5: Process coins.
def process_coins():
    """Takes coins and returns total"""
    total = 0
    print("Please insert coins")
    quarters = (int(input("How many quarters:"))) * 0.25
    dimes = (int(input("How many dimes:"))) * 0.10
    nickles = (int(input("How many nickles:"))) * 0.05
    pennies = (int(input("How many pennies: "))) * 0.01
    total = (quarters + dimes + nickles + pennies)
    return total


# TODO 6: Check transaction successful?
def is_transaction_successful(user_money, order_cost):
    """Checks that user inserted enough coins to make the drink.
    Returns true if money is sufficient. Returns user money if not sufficient. """

    global money
    if user_money < order_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        money += order_cost
        change = round(user_money - order_cost, 2)
        if change > 0:
            print(f"Here is $ {change} dollars in change.")
        return True


# TODO 7: Make Coffee.
def make_coffee(order_ingredients, coffee_resource):
    """Takes resources and order. Then processes the coffee after
    user has inserted enough coins and resources are available.
    Returns the remaining resources."""

    global resources
    for item in order_ingredients:
        remaining_resource = coffee_resource[item] - order_ingredients[item]
        resources[item] = remaining_resource
    # print (resources) for debugging purposes.
    print(f"Here is your {prompt}. Enjoy! ☕")


continue_dispensing = True

while continue_dispensing:
    # TODO 1: Prompt user “What would you like? (espresso/latte/cappuccino):”
    prompt = input("What would you like? (espresso/latte/cappuccino):")

    # TODO 2:  Turn off the Coffee Machine by entering “off” to the prompt.
    if prompt == "off":
        continue_dispensing = False

    # TODO 3: Print report.
    elif prompt == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")


    # TODO 4: Check resources sufficient?
    else:
        order = MENU[prompt]
        if check_resources(order["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, order["cost"]):
                make_coffee(order["ingredients"], resources)
