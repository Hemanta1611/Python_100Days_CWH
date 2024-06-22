# Python Decorators
'''
Python decorators are a powerful & versatile tool that allow you to modify the 
behavior of functions and methods. It ia a way to extend the functionality of 
a function or method without modifiying its source code.
'''

# here, greet() is decorator
def greet(function):
    def modified_function(x, y):
        print("Good Morning")
        function(x, y)
        print("Thanx for using this function.")
    return modified_function 

@greet  # a decorator
def add(a, b):
    print(f"{a} + {b} = {a+b}")

add(2, 7)   


# ⏬this will show error ⏬
# @greet
# def hello():
#     print("hello ji")
# hello()
# ⏫this will show error ⏫
# to fix this error 🐛 -->
"""
modify decorator as:
def modified_function(*x, **y):
    ..
    function(*x, **y)
    ..
return modified_function
"""



# *argument = tuple if we take this in a function
# **argument = dictionaries if we take this in a function



# import logging

# def log_function_call(func):
#     def decorated(*args, **kwargs):
#         logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}.")
#         result = func(*args, **kwargs)
#         logging.info(f"{func.__name__} returned {result}.")
#         return result
#     return decorated

# @log_function_call
# def my_function(a, b):
#     return a + b 

# sum = my_function(7,9)
# print(sum)