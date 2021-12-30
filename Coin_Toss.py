#Exploring the random module, this program presents a heads or tails outcome.
import random
coin_toss=random.randint(0,1)
print (coin_toss)
if coin_toss==1:
  print("Heads")
else:
  print("Tails")
