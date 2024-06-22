# Strings are immutable

a = "Hemanta"
print(a)
print(len(a))
print(a.upper()) #convert a into uppercase characters
print(a.lower()) #convert a into lowercase characters

b = "Hema!an$ta!!$$ !$$"
c = "Hema!an$ta!!$$"
print(b.rstrip("!$")) #removes any trailing characters
print(c.rstrip("!$")) #removes any trailing characters

print(a.replace("Hemanta", "Programmer"))
print(a) # hence proved strings are immutable

d = "silver spoon"
print(d.split()) #convert it into list

blogHeading = "introduction TO pythoN strIngs"
print(blogHeading.capitalize())  #capitalize the first letter and also correct the letter if any
print(blogHeading.title()) #capitalize the first letter of each word of the string
print(blogHeading.capitalize().center(50))  #center method is used to place the string into center with a parameter
print(len(blogHeading.center(90)))
print(blogHeading.count("i") + blogHeading.count("I"))

print(a.endswith("ta"))
print(a.startswith("Hem"))
print(blogHeading.find("to"))  #return -1 if it is not present in the string

d = "Hemanta7"
print(b.isalnum())
print(d.isalnum())
print(d.isalpha())
print(d.islower())
print(d.isupper())
print()
e = "hemanta\n" #backslash n is not a printable character
print(e.isprintable())

# isspace() return true iff strings has only white spaces else return false
# istitle() return true iff the first letter of each word of the string is capitalized, else return false
# swapcase() used to interchange the uppercase and lowercase


