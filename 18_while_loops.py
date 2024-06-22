count = 7
# while (count > 0):
#     print("count =", count)
#     count = count - 1

while (count > -7):
    print("count =", count)
    count = count -2
else:
    print("While loop over all conditioned satisfied & now it come inside else")


# do while loop in python : actually not present : we just make similar to that
# emulate( meaning: try to equal) of do while loop
i = 0
while True:
    print(i)
    i = i + 1
    if(i % 10 == 0):
        break