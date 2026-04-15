class Bird:
    def fly(self):
        print("Bird can fly")

class Sparrow(Bird):
    def fly(self):
        print("Can fly")

class Penguin(Bird):
    def fly(self):
        print("Cannot fly")

birds = [Sparrow(), Penguin()]

for b in birds:
    b.fly()
