# is and == both are comparision operator

a = 4
b = '4'

print(a is b)   # it compares exact location of object in memory
print(a == b)   # it comapars the value
print()

c = [1, 2, 3]
d = [1, 2, 3]

print(c is d)
print(c == d)

x = (1, 2)
y = (1, 2)

print()
print(x is y)
print(x == y)