'''
Python docstring are string literal that appear right after the definition of a function, 
method, class or module
'''

def square(n):
    '''Takes in a number n, returns the square
of n.'''
    print(n**2)

square(5)
print(square.__doc__)

def cube(m):
    print(m**3)
    '''Takes in a number n, returns the cube
of n.'''

cube(9)
print(cube.__doc__)


# PEP 8 -- Python Enhancement Proposal
# The Zen of Python - import this - it will give a poem
