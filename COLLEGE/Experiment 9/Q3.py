# Create programs to implement different types of inheritances.

# (A) Single Inheritance
class Parent:
    def show(self):
        print("This is Parent class")

class Child(Parent):
    def display(self):
        print("This is Child class")

c = Child()
c.show()
c.display()

# (B) Multilevel Inheritance
class Grandparent:
    def gp(self):
        print("Grandparent")

class Parent(Grandparent):
    def p(self):
        print("Parent")

class Child(Parent):
    def c(self):
        print("Child")

obj = Child()
obj.gp()
obj.p()
obj.c()

# (C) Multiple Inheritance
class A:
    def showA(self):
        print("Class A")

class B:
    def showB(self):
        print("Class B")

class C(A, B):
    def showC(self):
        print("Class C")

obj = C()
obj.showA()
obj.showB()
obj.showC()