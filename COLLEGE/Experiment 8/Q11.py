class User:
    def __init__(self, id):
        self.__id = id

    def get_id(self):
        return self.__id
class Student(User):
    def get_role(self):
        return "Student"

class Teacher(User):
    def get_role(self):
        return "Teacher"

u1 = Student(101)
u2 = Teacher(201)

print(u1.get_id(), u1.get_role())
print(u2.get_id(), u2.get_role())
