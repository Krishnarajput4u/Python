import student_utils
name=input("Enter the Name of the student: ")
num=int(input("Enter the number of the subjects: "))
marks=[]

for i in range(num):
    mark=int(input(f"Enter the mark of student in subject {i+1}: "))
    marks.append(mark)

average=student_utils.avg(marks)
print(f"The average marks are {average}")
grade=student_utils.grade(average)
print("Grade achieved is {grade}")
max=student_utils.maximum(marks)
print(f"The maximum number achieved in a subject is {max}")
min=student_utils.minimum(marks)
print(f"The minnimmum number achieved in a subject is {min}")
