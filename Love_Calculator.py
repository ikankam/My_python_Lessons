# Classic love calculator that tests the compatibility between two people.
# To do this, the user inputs their name and their partner's and checks for the number of times the letters in the words TRUE and LOVE occurs.
# This number is combined to make a two digit number.
# Based on this number, Love Scores less than 10 or greater than 90, prints the message:"Your score is x, you go together like coke and mentos."For Love Scores between 40 and 50, the message should be: "Your score is y, you are alright together." Otherwise, the message will just be their score. e.g.:"Your score is z."

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#Accepting names
name1_lower=name1.lower()
name2_lower=name2.lower()
print(name1_lower)
print(name2_lower)

#counting TRUE number for name 1
T_count=name1_lower.count('t')
R_count=name1_lower.count('r')
U_count=name1_lower.count('u')
E_count=name1_lower.count('e')

#counting TRUE number for name 2
T_count2=name2_lower.count('t')
R_count2=name2_lower.count('r')
U_count2=name2_lower.count('u')
E_count2=name2_lower.count('e')

#Finding the total for TRUE
Total_True=T_count+T_count2+R_count+R_count2+U_count+U_count2+E_count+E_count2
print(Total_True)

#counting LOVE number for name 1
L_count=name1_lower.count('l')
O_count=name1_lower.count('o')
V_count=name1_lower.count('v')
E_count=name1_lower.count('e')

#counting TRUE number for name 2
L_count2=name2_lower.count('l')
O_count2=name2_lower.count('o')
V_count2=name2_lower.count('v')
E_count2=name2_lower.count('e')


#Finding the total for LOVE
Total_Love=L_count+L_count2+O_count+O_count2+V_count+V_count2+E_count+E_count2
print(Total_Love)

#Concatenation
Num_cat=str(Total_True)+str(Total_Love)
print(Num_cat)
Num=int(Num_cat)

#Condition
if (Num<10) or (Num>90):
  print (f'Your score is {Num}, you go together like coke and mentos.')
elif Num>=40 and (Num<=50):
  print (f"Your score is {Num}, you are alright together.")
else:
    print(f"Your score is {Num}.")
