# 1.Create a class of student (name, sap id, marks[phy,chem,maths] ). Create 3 objects by
# taking inputs from the user and display details of all students.

class Student:
    def __init__(self, name, sap_id, marks):
        self.name = name
        self.sap_id = sap_id
        self.marks = marks

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"SAP ID: {self.sap_id}")
        print(f"Marks: {self.marks}")

students = []
for i in range(3):
    name = input("Enter student name: ")
    sap_id = input("Enter student SAP ID: ")
    marks = list(map(int, input("Enter marks for Physics, Chemistry, Maths (separated by space): ").split()))
    student = Student(name, sap_id, marks)
    students.append(student)

for student in students:
    student.display_details()