# MAP
def cube(x):
    return x*x*x

print(cube(2))

l = [1, 2, 5, 6, 7, 9]

newL = []
for item in l:
    newL.append(cube(item))

print(newL)
newL2 = list(map(cube, l))
print(newL2)
newL3 = list(map(lambda x: x*x, l))
print(newL3)
print()



# FILTER
def filter_function(a):
    return a > 4

newL4 = list(filter(filter_function, l))
print(newL4)

newL5 = list(filter(lambda x: x > 6, l))
print(newL5)
print()



# REDUCE
from functools import reduce as rd

numbers = [1, 2, 3, 4, 5, 6, 7]
# 1 + 2 = [3, 3, 4, ..]
# 3 + 3 = [6, 4, 5, ..]
# 6 + 4 = [10, 5, 6, .] 

# calculate the sum of numbers using the reduce function
sum = rd(lambda x, y: x + y, numbers)

print("sum:", sum)

