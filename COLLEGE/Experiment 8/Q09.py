from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class CreditCard(Payment):
    def pay(self):
        print("Paid using Credit Card")

class UPI(Payment):
    def pay(self):
        print("Paid using UPI")

p1 = CreditCard()
p2 = UPI()

p1.pay()
p2.pay()
