import time

timestamp = time.strftime('%H:%M:%S')
print("Current time:", timestamp)

# timestamp = time.strftime('%H')
# print(timestamp)

# timestamp = time.strftime('%M')
# print(timestamp)

# timestamp = time.strftime('%S')
# print(timestamp)

hour = time.strftime('%H')
if(int(hour) >= 5 and int(hour) < 12):
    print("Good Morning Dear Pandu")
elif(int(hour) == 12):
    print("Good Noon Dear Pandu")
elif(int(hour) > 12 and int(hour) < 16):
    print("Good AfterNoon Dear Pandu")
elif(int(hour) >= 16 and int(hour) < 20):
    print("Good Evening Dear Pandu")
else:
    print("Good Night Dear Pandu")

# instead writing int(hour) every time we can write as: hour = int(time.strftime('%H'))