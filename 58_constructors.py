class Person:
    def __init__(self, name, o):
        print("Hey I am a Programmer.")
        self.name = name
        self.occupation = o

    def info(self):
        print(f"{self.name} is a {self.occupation}.")

    # info(self) #it will show error as self is not defined

a = Person("Hemanta", "System Engineer")
b = Person("Madhuri", "Teacher")
a.info()
b.info()
print(a.occupation) # print(a.o) will show error



# __init__ is a special method which helps us to make a contructor or we can say __init__ is known as contructor in oop


class FileManager:
    def __init__(self, filename):
        self.file = open(filename, "r")

# Create a new FileManager object
file_manager = FileManager("myfile58.txt")

# Read the contents of the file
file_contents = file_manager.file.read()

# Print the file contents
print(file_contents)