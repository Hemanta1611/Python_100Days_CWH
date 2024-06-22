class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"The name is {self.name}.")

class Dancer:
    def __init__(self, dance):
        self.dance = dance

    def show(self):
        print(f"The dance is {self.dance}.")

class DancerEmployee(Employee, Dancer):
    def __init__(self, name, dance):
        Employee.__init__(self, name)
        Dancer.__init__(self, dance)
        # self.dance = dance
        # self.name = name

o = DancerEmployee("Ankit", "Kathak")
print(o.name, "love to dance on" , o.dance)
o.show() # it will use show method from 1st called/inherited class
print(DancerEmployee.mro()) # method resolution order

