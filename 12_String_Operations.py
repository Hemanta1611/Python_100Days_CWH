name = "Hemanta, Program"
print("First 7 letters of \"name\":", name[0:7])
print(name[:7])

print(name[:])

# print(name[0:-3]) ===== print(name[0:len(name)-3])

print("Length of name:", len(name))

print(name[0:-3])
print(name[-3:])

print(name[::-1]) #print opposite of string

a = "aeroplane"
print(a[5:8][::-1])

print(id(a[0])) #address of index 0 and character a
print(id(a[6])) #address of index 6 and character a