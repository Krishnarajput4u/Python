#  Create a class to implement method Overriding.

class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def show(self):
        print("Child method (Overridden)")

obj = Child()
obj.show()
