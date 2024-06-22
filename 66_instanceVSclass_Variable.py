class Employee:
    companyName = "Apple" # class variable --> same for all object
    def __init__(self, name):
        self.name = name  # instance variable --> different for different object
        self.raise_amount = 0.02  # instance variable --> different for different object
    def showDetails(self):
        print(f"The name of the Employee is {self.name} and the raise amount in {self.companyName} is {self.raise_amount}.")
    

emp1 = Employee("Hemanta")
emp1.raise_amount = 0.2
emp1.companyName = "Apple India"
emp1.showDetails()
emp2 = Employee("Rohan")
emp2.showDetails()
