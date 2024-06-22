class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def area(self):
        return self.x * self.y
    
# class Circle(Shape):
#     def __init__(self, radius):
#         self.randius = radius
#     def area(self):  # method overriding
#         return 3.14 * self.randius * self.randius

class Circle(Shape):
    def __init__(self, radius):
        self.randius = radius
        super().__init__(radius, radius)
    def area(self):  # method overriding
        return 3.14 * super().area()
    

rect = Shape(2,7)
print("Area of Rectanle:", rect.area())

cir = Circle(7)
print("Area of the Circle is:", cir.area())