# Class Methods as alternative constructors
# it is just as class method just acting little as constructor not completly as constructor
class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    @classmethod
    def fromStr(cls, string):
        return cls(string.split("-")[0], string.split("-")[1])
    
    @classmethod
    def from_string(cls, string):
        name, salary = string.split(',')
        return cls(name, int(salary))


e1 = employee("sandeep", 12000)
print(e1.name)
print(e1.salary) 
print()


string = "Dinesh-6000"
e2 = employee(string.split("-")[0], string.split("-")[1])
print(e2.name)
print(e2.salary)
print()

string1 = "saurabh-150"
e3 = employee.fromStr(string1)
print(e3.name)
print(e3.salary)
print()

string2 = "vardhan,9000"
e4 = employee.from_string(string2)
print(e4.name)
print(e4.salary)
print()