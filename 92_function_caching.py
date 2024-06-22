import functools
import time

# Memoization is an optimization technique used to speed up computer programs by caching the results 
# of expensive function calls and returning them when the same inputs are encountered again
@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*5

print(fx(20))
print("done for 20") # it will print after 5 sec
print(fx(2))
print("done for 2") # it will print after 5 sec
print(fx(6))
print("done for 6") # it will print after 5 sec


# it will print at a time 
print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")
print(fx(69))
print("done for 69")


