#8.	Print the grade sheet of a student for the given range of cgpa. Scan marks of five subjects and calculate the percentage.
name = input("Enter Name: ")
roll = input("Enter Roll Number: ")
sapid = input("Enter SAP ID: ")

m1 = int(input("Enter PDS marks: "))
m2 = int(input("Enter Python marks: "))
m3 = int(input("Enter Chemistry marks: "))
m4 = int(input("Enter English marks: "))
m5 = int(input("Enter Physics marks: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5
cgpa = percentage / 10

if cgpa <= 3.4:
    grade = "F"
elif cgpa <= 5.0:
    grade = "C+"
elif cgpa <= 6.0:
    grade = "B"
elif cgpa <= 7.0:
    grade = "B+"
elif cgpa <= 8.0:
    grade = "A"
elif cgpa <= 9.0:
    grade = "A+"
else:
    grade = "O (Outstanding)"

print("\n----- GRADE SHEET -----")
print("Name:", name)
print("Roll Number:", roll, "SAP ID:", sapid)
print("Percentage:", percentage, "%")
print("CGPA:", cgpa)
print("Grade:", grade)
