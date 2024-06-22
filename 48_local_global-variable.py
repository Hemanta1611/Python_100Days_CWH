x = 4 # Global Variable
print(x)

def hello():
    x = 5 # Local Variable
    global y # Globar VAriable
    y = 9
    print(f"The local x is {x}")
    print("hello hemanta")

print(f"The global x is {x}")
hello()
print(f"The global x is {x}")
print(y)

