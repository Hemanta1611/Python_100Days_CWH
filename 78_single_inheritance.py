"""
Single Inheritance:
-->Single Inheritance is a type of inheritance where a class inherits
properties and behaviours from a single parent class. This is the simplest
and most common form of inheritance.
"""

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def show(self):
        print(f"{self.name} is having id number {self.id}.")


class Programmer(Employee):
    def showLang(self):
        print("The default language is Python")


emp = Employee("Ankit", 6969)
emp.show()
# emp.showLang() # it will show error

emp2 = Programmer("Rahul", 9696)
emp2.show()
emp2.showLang()
