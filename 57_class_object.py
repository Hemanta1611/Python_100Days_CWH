class Person:
    name = "Hemanta"
    occupation = "System Engineer"
    net_worth = 9999999772
    def info(x):
        print(f"{x.name} is a {x.occupation}.")
# x is a reference to the current instance of the class, and is used to access variable that belongs to the class
    

a = Person()
print(a.name, a.occupation, a.net_worth)
a.info()

b = Person()
b.name = "Madhuri"
b.occupation = "Teacher"
print(b.name, b.occupation)
b.info()

