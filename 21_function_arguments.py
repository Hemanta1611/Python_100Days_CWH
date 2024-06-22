def average(a, b = 7):
    print("The average is", (a+b)/2)

average(a = 21)
average(b = 3, a = 8)

# '*' before the parameter name while defining the function.
# the function access the arguments by processing them in the form of tuple

def Average(*num):
    print("Type of '*' argument:", type(num))
    sum = 0
    for i in num:
        sum = sum + i
    print("tuple:", num)
    print("Average is:", (sum/len(num)))


Average(1, 2, 3, 4, 5, 6, 7, 8, 9)


# '**' is used to take argument as dictionary

def name(**names):
    print("Type of ** names:", type(names))
    print("Hello", names["Fname"], names["Mname"],names["Lname"])

name(Fname = "Hemanta", Mname = 'Kumar', Lname = 'Bhoi')

print()
def Average(*num):
    # print("Type of '*' argument:", type(num))
    sum = 0
    for i in num:
        sum = sum + i
    print("tuple:", num)
    return sum / len(num)

c = Average(1, 2, 3, 4, 5, 6, 7, 8, 9)
print("Average of numbers:", c)