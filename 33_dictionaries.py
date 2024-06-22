dict1 = {"name":"Hemanta", "age":"20", 'canVote': True, "sign": 'H'}
print(dict1)
print(type(dict1))
print()
print("Name:", dict1["name"])   # it will give error if item is not present
print("Name:", dict1.get("name"))   # it will not give any error even if the item is not present

print("Keys:",dict1.keys())
print("Values:",dict1.values())
print()

for key in dict1.keys():
    print("Key:",key)
    print("Values:",dict1[key])
    print()

print("Items:", dict1.items())
for key, value in dict1.items():
    print("Key:",key)
    print("Values:",value)
    # print("Values:", dict1[key])
    print()


