#This program will mark a spot with 'X' based on user input. Eg: User enters 23
# This indicates column 2 row 3 and marks this spot with X to hide the treasure.

row1 = ["⬜","⬜","⬜"]
row2 = ["⬜","⬜","⬜"]
row3 = ["⬜","⬜","⬜"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

#Getting user location to hide the treasure
position = input("Where do you want to put the treasure? ")

#changing to corresponding indices
index_one=position[0]
index_two=position[1]

# obtaining location
Row=map[int(index_two)-1]
Row[int(index_one)-1]='X'

#printing output
print(f"{row1}\n{row2}\n{row3}")