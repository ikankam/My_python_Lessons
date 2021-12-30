# Program selects a random name from a list of user given names and outputs who will pay everyone's bill.
# Exploring random module on a list
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
random_name=random.randint(0,len(names)-1)
print(names[random_name] + ' is going to buy the meal today!')