class Parent:
    def __init__(self, name, id):
        self.name = name 
        self.id = id
    def parent_method(self):
        print("This is the parent method.")

class Child(Parent):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang
    def child_method(self):
        print("This is the child method.")
        super().parent_method()

parent_object = Parent()
parent_object.parent_method()
print()
child_object = Child()
child_object.child_method()

