"""
Access Specifiers/ Modifiers
--> access specifiers/modifiers in python programming are used to limit the access of class
variable and class methods outside of class while implementing the concepts of inheritance

Types of Access Specifiers:
1. Public Access modifiers
2. Private Access modifiers  --> double underscore 
3. Protected Access modifiers


"""

class Employee:
    def __init__(self):
        self.__name = "Hemanta" # private
        self._title = "Bhoi"

a = Employee()
# print(a.__name) # can't be accessed directly
print(a._Employee__name) # can be accessed in-directly
print(a.__dir__()) # the methods which can be applied and used will shown by this
print(a._title)  # can be accessed directly


"""
In Python, there are two types of underscores that can be used when naming variables and attributes: 
single underscores (_) and double underscores (__).

Single Underscore

A single underscore before a variable or attribute name is a naming convention that indicates that it is for internal use only.
This means that it should not be accessed or modified directly from outside of the class or module in which it is defined.

For example, a class might have a private attribute named _name that stores the name of the class instance. 
This attribute would be intended for use only by the class itself, and other code should not access it directly.

However, it is important to note that the single underscore is just a naming convention, 
and there is nothing actually preventing code from accessing or modifying private variables and attributes.

Double Underscore

A double underscore before a variable or attribute name is a special naming convention that tells the Python interpreter to modify the name of the variable or attribute.
This process is known as name mangling, and it is used to avoid naming conflicts between variables and attributes in different classes.

For example, if a class defines an attribute named __name__, this attribute will be automatically renamed to _ClassName__name__ by the Python interpreter. 
This helps to prevent conflicts with the name attribute that is defined in the object class, which is the base class for all Python classes.

Name mangling is also used for special methods in Python, which are methods that have names that start and end with double underscores. 
These methods are used by the Python interpreter to implement various features of the language, such as magic methods and operator overloading.

In general, it is best to avoid using double underscores in your own code, unless you are specifically implementing a special method or need to avoid a naming conflict."""


