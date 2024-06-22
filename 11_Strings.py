# In Python, anything that we encloses between single or double quotes is considered as string.
name = "Hemanta Kumar Bhoi"
friend = "Madhuri Bhoi"
anotherFriend = 'Prabhat Bhoi'
AnotherFriend = 'Manju Bhoi' 

print("Hello1", name, sep = "   ")
print("Hello2 " + name)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6] + "\n")
# print(name[18])

print("Lets use a for loop:")
for character in name:
    print(character)


random_text = "I'm Hemanta."
random_Text = "I\'m Hemanta."
# random_textt = 'I'm Hemanta.'  # this will show error as we can't use same quote in a single string


# Multi-Line String
hello = '''
He said,
Hi Hemanta
How are you??'''
# OR
hello2 = """He said,
Hi Hemanta
How are you??
"""
print("\n")
print("Lets use a for loop:")
for char in hello:
    print(char)
print(hello)
print(hello2)