"""
class BaseClass:
    Body of base class
class DerivedClass(BaseClass):
    Body of derived class
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


"""
Types of Inheritance:
1. Single Inheritance
2. Multiple Inheritance
3. Multilevel Inheritance
4. Hireachical Inheritance
5. Hybrid Inheritance
"""