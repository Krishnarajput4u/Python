class Student():
    def __init__(self):
        self.name="rahul"
        self.__marks=90

s=Student()
print("s.name")
print(s._Student__marks) # Important