# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total_heights = sum(student_heights)
number_of_students = len(student_heights)
avarage_heights = round(total_heights/number_of_students)
print(avarage_heights)