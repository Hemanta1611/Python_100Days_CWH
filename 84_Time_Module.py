import time

def usingWhile():
    i = 0
    while i < 1000:
        print(i)
        i = i + 1
"""
(function) def time() -> float
time() -> floating point number

Return the current time in seconds since the Epoch. 
Fractions of a second may be present if the system clock provides them."""

init = time.time()
# usingWhile()
totaltime1 = time.time() - init
# print(totaltime1)

def usingFor():
    for i in range(1000):
        print(i)

init2 = time.time()
# usingFor()
totaltime2 = time.time() - init2
# print(totaltime2)

# print(totaltime1 - totaltime2)



print("random line printed just now")
time.sleep(7) # sleep for seven second
print("printed after 7 second")


# for one more example go to excercie2: 15_26_ex-2.py

current_time = time.strftime("%d-%m-%Y %H:%M:%S")
print(current_time)

