class Father:
    def skills(self):
        print("Driving")

class Mother:
    def talent(self):
        print("Cooking")

class Child(Father, Mother):
    pass

c = Child()
c.skills()
c.talent()