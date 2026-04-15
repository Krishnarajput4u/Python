class Vehicle:
    def run(self):
        print("vechile is Running")

class Car(Vehicle):
    def run(self):
        print("car is Running") 

c=Car()
c.run()