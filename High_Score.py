# This program uses the for loop to calculate the max or highest score in a list.

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

dummy_score=0
for score in student_scores:
    if score>dummy_score:
        dummy_score=score
print (f"The highest score in the class is: {dummy_score}")