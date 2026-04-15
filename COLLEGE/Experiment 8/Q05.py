class Person:
    def __init__(self,name):
        self.name=name

class Employee(Person):
    def __init__(self, name,salary):
        super().__init__(name)

        self.salary=salary

class Manager(Employee):
    def __init__(self, name, salary,dept):
        super().__init__(name, salary)
        self.dept=dept

m=Manager("amit",50000,"IT")

print(m.name,m.salary,m.dept)