class MyClass:
    def __init__(self, value):
        self._value = value
    def show(self):
        print(f"Value is: {self._value}")

    @property
    def new_value(self):
        return 2 * self._value
    
    @new_value.setter
    def new_value(self, new_value):
        self._value = new_value * 10



obj = MyClass(9)
obj.new_value = 69 # it will show error if we don't use {setter}
print(obj.new_value)
obj.show()

