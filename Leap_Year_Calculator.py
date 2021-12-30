# Determines whether a year is a leap year or not.
#This program explores control flows and logical statements. It accepts a year from user and converts to integer.
#It then determines whether a year is a leap year or not.

# accepts year from user and converts to integer
year = int(input("Which year do you want to check? "))

if year%4==0:
  if year%100==0:
    if year%400==0:
      print ("Leap Year")
    else:
        print ("Not a leap year")
  else:
      print ("Leap year")
else:
      print ("Not a leap year")

