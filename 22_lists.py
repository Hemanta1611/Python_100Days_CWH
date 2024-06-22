lists = [3, 5, 6, "8"]
print(lists)
print(type(lists))
print()

if 7 in lists:
    print("Yes")
else:
    print("No")
if 8 in lists:
    print("Yes")
else:
    print("No")
if "6" in lists:
    print("Yes")
else:
    print("No")
print()

# list comprehension
lst = [i*i for i in range(1, 10, 2)]
print(lst)

list = [i*i for i in range(10) if i%2==0]
print(list)
