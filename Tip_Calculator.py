print("Welcome to the tip calculator!")
Total_bill=int(input("What was the total bill?"))
Tip=int(input("How much tip would you like to give? 10, 12 or 15"))
Num_of_peep=int(input("How many people to split the bill?"))
Each_person_pays= ((Total_bill* (Tip/100))+Total_bill)/Num_of_peep
print (str(Each_person_pays))
Amount=format (Each_person_pays, '.2f')
print (Amount)