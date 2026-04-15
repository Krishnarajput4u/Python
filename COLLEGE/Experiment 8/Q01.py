class Animal:
    def sound(self):
        print("animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Barks")

d=Dog()
a=Animal()
a.sound()
d.sound()