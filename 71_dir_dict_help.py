x = [1, 2, 3]
# print(dir(x))
# dir method shows total methods we can perform on x:
"""     ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__',
'__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__',
'__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', 
'__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', 
'__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 
'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']      """

print()
print(x.__add__)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

print("\n")
p = Person("Jhon", 30)
print(p.__dict__)   # this __dict__ method is used to make something into dictionary
# print(dir(Person))  

# print(help(str))
# print(help(x))
# print(help(Person))
# print(help(PermissionError))


