s1 = {1, 2, 5, 7, 9, "H"}
s2 = {3, 6, 7, 9, "H"}

print("UNION:   ",s1.union(s2))
# print(s1.update(s2))

print("INTERSECTION:    ",s1.intersection(s2))
# print(s1.intersection_update(s2))

print("SYMMETRIC DIFFERENCE:    ",s1.symmetric_difference(s2)) # = (a union b) - (a interssection b) 
# print(s1.symmetric_difference_update(s2))

print("DIFFERENCE:    ",s1.difference(s2)) # = (a - b) = (a) - (a intersection b)
# print(s1.difference_update(s2))

print("Disjoint or not:    ", s1.isdisjoint(s2))
print("Superset or not:    ", s1.issuperset(s2))
print("Subset or not:    ", s1.issubset(s2))

s1.add("B")     # add one item
print('New set s1:     ',s1)
s1.update([3, 6, "K"]) # add more than one item
print('New set s1:    ', s1)
s1.remove("B") # remove when element is present else shows errors
s1.discard("L") # don't show error and also remove elements if present
s1.pop() # random value popped
# del s1 # to delete the set
# s1.clear() # to clear / empty the set

# if item in set:
#     print("present")
# else:
#     print("not present")