# to make custom data type we use class 
# we can say class is extend of structure(in c)

class employee:
    company = "apple"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}.")

    def changeCompany(cls, newCompany):
        cls.company = newCompany

    @classmethod
    def changecompany(aloo, newcompany):
        aloo.company =newcompany


e1 = employee()
e1.name = "hemanta"
e1.show()
e1.changeCompany("tesla") # this method will not change value of class variable , its just create and give instance variable
e1.show()
print(employee.company)
print()

e1.changecompany("tesla") # this method will change value of class variable by the help of classmethod decorator
e1.show()
print(employee.company)