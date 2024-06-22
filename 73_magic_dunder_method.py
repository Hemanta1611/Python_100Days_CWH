class Employee:
    name = "Dinesh"
    def len(self): # not a magic method 
        i = 0
        for c in self.name:
            i = i + 1
        return i
    
    def __len__(self): # magic method 
        i = 0
        for c in self.name:
            i = i + 1
        return i
    
    def __str__(self):
        return f"The name of the employee is {self.name}. {{str}}"
    def __repr__(self):
        return f"The name of the employee is {self.name}. {{repr}}"
    
    def __call__(self):
        print("Hey I am good.")

e1 = Employee()
print(e1.name)
print(e1.len()) # not magic 
print(len(e1)) # magic

print(e1) # if we comment out __str__ then it will fall down to __repr__ and give output of __repr__
e1() # using __call__ magic method

"""
In Python, the presence of a double underscore (__) before and after a name in a class is an indication 
that it might be a special method, also known as a "magic" or "dunder" method (short for "double underscore"). 
These methods have a specific meaning and are called by the Python interpreter in certain situations.

For example, __init__ is a special method used for initializing objects, and __str__ is a special method 
used to represent an object as a string. The double underscores serve as a way to avoid naming conflicts 
with user-defined attributes and methods.

To know whether __abc__ is a valid special method inside a class, you can refer to the Python documentation or 
other reliable sources like PEP (Python Enhancement Proposal) documents. In general, special methods have 
a well-defined purpose and behavior, so using them according to their intended purpose is considered valid.

Here are some examples of commonly used special methods:

__init__: Initialize an object.
__str__: Return a string representation of an object.
__repr__: Return a string representation that can be used to recreate the object.
__len__: Return the length of an object.
__getitem__: Get an item from an object using square bracket notation.
__setitem__: Set an item in an object using square bracket notation.
__delitem__: Delete an item from an object using square bracket notation.

Always refer to the Python documentation or relevant PEPs to confirm the validity and purpose of a specific special method.
"""