# if we use static method then we can create method without using self argument

class Math:
    def __init__(self, num):
        self.num = num
    
    def addtwonum(self, n):
        self.num = self.num + n
    
    @staticmethod
    def add(a, b): # here a will not act as self
        return a+b
    
    # def sub(c, d): # here c will act as self 
    #     return c - d # it will show error because c will act as self 
    
a = Math(7)

print(a.num)
a.addtwonum(9)
print(a.num)

print(a.add(2,7))
print(Math.add(2,7))

print(a.sub(9,7))
