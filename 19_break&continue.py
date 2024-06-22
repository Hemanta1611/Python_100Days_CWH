num = int(input("Enter a number you want multiplication table of "))

for i in range(1,21):
    print("5 X", i, "=", num*i)
    if(i == 10):
        break


for i in range(1,21):
    if(i == 11):
        break
    elif(i % 2 == 1):
        print("             Iteration Skipped La La")
        continue
    else:
        print("5 X", i, "=", num*i)

# break is used to get out from the loop or we can say loop breaks

# continue is used to skip any interation in the loop

