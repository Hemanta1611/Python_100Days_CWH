with open('myfile51.txt', 'r') as f:
    print(type(f))
    f.seek(10) # move to the 10th byte/character in the file or skip 10 characters
    data = f.read(5) # read the next 5 character
    print(data)
    print(f.tell()) # it returns the current position within the file



with open('myfile51w.txt', 'w') as f:
    f.write("Hello World\n")
    f.truncate(5)

with open('myfile51w.txt') as f:
    print(f.read())


