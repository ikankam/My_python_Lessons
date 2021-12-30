# Program to calculate average height of students.
# User enters a list of students and program calculates the average. Exploring for loop
Total_height= 0
num_of_students=0
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  Total_height+=student_heights[n]
  num_of_students += 1
print (f"Sum of student heights: {Total_height}")
print (f"Number of students entered: {num_of_students}")
Average=Total_height/num_of_students
print (f"Average of student heights: {round(Average)}")
