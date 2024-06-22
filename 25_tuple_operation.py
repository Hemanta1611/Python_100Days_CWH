countries = ("Spain", "Italy", "India", "England", "Germany")

temp = list(countries) # convert tuple to list
temp.append("Russia") # add item
temp.pop(3) # remove item
temp[2] = "Finland" # change or replace item with new item
countries = tuple(temp) # convert list to tuple
print(countries)

# index method
# special index method: tuple.index(element, start, end)
# count method
