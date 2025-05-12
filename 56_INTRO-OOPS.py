"""
Introduction to Object-Oriented Programming (OOP) in Python

Object-Oriented Programming is a programming paradigm that uses objects to design applications and computer programs.
It provides a clear structure for the programs and helps to keep the code DRY (Don't Repeat Yourself).

Key Concepts of OOP:

1. Classes and Objects:
   - A class is a blueprint for creating objects
   - An object is an instance of a class
   - Objects have attributes (data) and methods (functions)

2. Four Pillars of OOP:
   a) Encapsulation:
      - Bundling of data and methods that operate on that data
      - Restricting access to some of the object's components
   
   b) Inheritance:
      - Creating a new class from an existing class
      - Reusing code and establishing relationships between classes
   
   c) Polymorphism:
      - Ability to use a single interface for different underlying forms
      - Same method name can behave differently for different objects
   
   d) Abstraction:
      - Hiding complex implementation details
      - Showing only necessary features of an object

Basic Example:
"""


# Example of a simple class
class Dog:
    # Class attribute (shared by all instances)
    species = "Canis familiaris"
    
    # Constructor method (__init__)
    def __init__(self, name, age):
        # Instance attributes (unique to each instance)
        self.name = name
        self.age = age
    
    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"
    
    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

# Creating objects (instances) of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# Using the objects
print(dog1.description())  # Output: Buddy is 3 years old
print(dog2.speak("Woof!"))  # Output: Max says Woof!

"""
This is a basic introduction to OOP in Python. The following files will cover more advanced concepts
and practical examples of OOP implementation.
"""