student_scores = input("Input a list of student scores ").split()

for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# on below syntax n is replaced woth arrey and student scores with counter to find the data type.

# arrey = input('Enter scores').split()

# for counter in range (0, len(arrey)):
#   print(f"{arrey[counter]} is of type - {type(arrey[counter])}")
#   arrey[counter] = int(arrey[counter])
#   print(f"{arrey[counter]} is of type - {type(arrey[counter]}")

print(student_scores)

highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score 
print(f"The highest score in the class is {highest_score}")