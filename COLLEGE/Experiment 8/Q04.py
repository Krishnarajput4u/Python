from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def area(self):
        return "Area of Rectangle"
    
r=Rectangle()
print(r.area())