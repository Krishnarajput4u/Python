class Distance:
    def __init__(self, d):
        self.d = d

    def __add__(self, other):
        return self.d + other.d

d1 = Distance(10)
d2 = Distance(20)

print(d1 + d2)
