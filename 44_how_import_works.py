# import this

import math

result = math.sqrt(69)
print(result)

from math import sqrt, pi

result2 = sqrt(69)
print(result2, "\n")

from math import *      # import all function and variable

# import math as mh 
# from math import pi, sqrt as sq

print("Description: ", dir(math))
print(type(math.frexp))
print(type(math.comb))
print(type(math.nan))


print()
# from template44 import welcome, Hemanta 
# from template44 import *    

# welcome()
# print(Hemanta)

import template44 as tp 
tp.welcome()
print(tp.Hemanta)

