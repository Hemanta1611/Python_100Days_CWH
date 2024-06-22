'''
a = 134131351398798749
print(a)
print(type(a))
print("\n")

b = True
print(b)
print(type(b))
print("\n")

c = "Hemanta"
print(c)
print(type(c))
print("\n")

d = 'H'
print(d)
print(type(d))
print("\n")

e = 2.7
print(e)
print(type(e))
print("\n")

f = None
print(f)
print(type(f))
print("\n")

g = complex(2, 7)
print(g)
print(type(g))
print("\n")

list1 = [8, 2.3, [[-7, 9], ["apple", "banana"]]]
print(list1)
print(type(list1))
print("\n")

tuple1 = (("Parrot", "Sparrow"), ("Lion", "Tiger"))
print(tuple1)
print(type(tuple1))
print("\n")

dict1 = {"name":"Hemanta", "age":"20", 'canVote': True, "sign": 'H'}
print(dict1)
print(type(dict1))
print("\n")
'''
# strings are immutable and tuple are also immutable
# lists are mutable

list2 = [2, 4, 6]
print(list2)
list2.append("for")  # we can append only 1 argument at a time
print(list2)
print(list2[3][2])
print(type(list2[3][2]))

list2.insert(1, 3) # insert(index, element)
print(list2)

# list2[4].insert(3, "each")    # no insert method for strings as list2[4] is a string
# print(list2)

list2.extend(['a', 'e', 'i']) # we can extend any number of argument at a time
print(list2)

list2.remove("for") 
print(list2)

list2.pop() # it will pop last element
print(list2)