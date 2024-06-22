# function to double the input
def double(x):
    return x * 2

# Lambda function to double the input
twice = lambda x: x * 2

print(double(69))
print(twice(69))

average = lambda x, y: (x + y) / 2
print(average(69, 96))

print(type(average))


# we can pass function inside a function 
def random(fx, value):
    return 7 + fx(value)

print(random(double, 69))   # ans = 7 + double(69)
print(random((lambda x: x * x * x), 5)) # ans = 7 + 5*5*5


