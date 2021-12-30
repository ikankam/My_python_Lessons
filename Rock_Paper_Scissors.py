# Classical Rock, paper, scissors game. Practicing debugging skills where user enters  number outside the given list.

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


Choices= [rock, paper, scissors]
User_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if User_choice>=3 or User_choice<0:
  print ("You lose. Enter a valid number")
else:
  show_choice=Choices[User_choice]
  print (f'(You chose {User_choice})'+ show_choice)
  Random_choice=random.randint(0,2)
  Computer_choice=Choices[Random_choice]
  print(f'(Computer chose {Random_choice})' + Computer_choice)
  if User_choice==0 and Random_choice==2:
    print("Rock wins against scissors. You win!")
  elif User_choice==2 and Random_choice==0:
      print("Rock wins against scissors. You lose!")
  elif User_choice==2 and Random_choice==1:
      print("Scissors wins against paper. You win!")
  elif User_choice==1 and Random_choice==2:
      print("Scissors wins against paper. You lose!")
  elif User_choice==1 and Random_choice==0:
      print("Paper wins against rock. You win!")
  elif User_choice==0 and Random_choice==1:
      print("Paper wins against rock. You lose!")
  else:
        print("Its a draw.")

