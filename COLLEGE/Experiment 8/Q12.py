from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, id):
        self.__id = id

    @abstractmethod
    def display_info(self):
        pass

class Book(LibraryItem):
    def display_info(self):
        print("This is a Book")

class Magazine(LibraryItem):
    def display_info(self):
        print("This is a Magazine")

items = [Book(1), Magazine(2)]
for item in items:
    item.display_info()
