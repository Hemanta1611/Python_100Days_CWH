# we can create a generator by using the {{yield]] statement in a function

def my_generator():
    for i in range(5):
        yield i 

gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen))



