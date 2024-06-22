def factorial(num):
    if(num == 1 or num == 0):
        return 1
    else:
        return num * factorial(num - 1)
    
num = int(input("Enter a number you want factorial of: "))
print(f"Factorial of {num} is:", factorial(num))


def fibonacci(n):
    if(n == 1):
        return 0
    elif(n == 2):
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
n = int(input("Enter a number to print fibonacci at given number location: "))
print(f"Fibonacci at location {n} is:", fibonacci(n))