# . Add constructor in the above class to initialize student details of n students and implement following methods:
# a)	Display() student details
# b)	Find Marks_percentage() of each student
# c)	 Display result() [Note: if marks in each subject >40% than Pass else Fail]
# d)	Write a Function to find average of the class.


class Student:
    def __init__(self, name, sap_id, phy, chem, maths):
        self.name = name
        self.sap_id = sap_id
        self.phy = phy
        self.chem = chem
        self.maths = maths

    def display(self):
        print("\nName:", self.name)
        print("SAP ID:", self.sap_id)
        print("Marks:", self.phy, self.chem, self.maths)

    def marks_percentage(self):
        total = self.phy + self.chem + self.maths
        return total / 3

    def result(self):
        if self.phy > 40 and self.chem > 40 and self.maths > 40:
            return "Pass"
        else:
            return "Fail"


# Taking input for n students
n = int(input("Enter number of students: "))
students = []

for i in range(n):
    print(f"\nEnter details for student {i+1}")
    name = input("Name: ")
    sap = input("SAP ID: ")
    phy = int(input("Physics: "))
    chem = int(input("Chemistry: "))
    maths = int(input("Maths: "))

    s = Student(name, sap, phy, chem, maths)
    students.append(s)


# Display + Results
total_class = 0

for s in students:
    s.display()
    perc = s.marks_percentage()
    total_class += perc
    print("Percentage:", perc)
    print("Result:", s.result())


# Class average
avg = total_class / n
print("\nClass Average:", avg)
