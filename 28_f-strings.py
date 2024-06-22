# letter = "Hey my name is {1} and I am from {0}"
# country = "India"
# name = "Hemanta"
country = input()
name = input()

# print(letter.format(country, name))
print(f"Hey my name is {name} and I am from {country}")


price = 49.099999
txt = f"Only for{price: .2f} rupees!"
print(txt)

print(type(f"{2 * 7}"))

# to show curli braces inside print then use two curli braces
print(f"{{Hemanta}}")
