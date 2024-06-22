age = int(input("Enter your age: "))
print("Your age is:", age)

# print(age > 18)
# print(age >= 18)
# print(age < 18)
# print(age <= 18)
# print(age == 18)
# print(age != 18)


# if(age >= 18):
#     print("You are eligible for vote.")
# else:
#     print("You are not eligible for vote")


# budget = int(input("Enter your budget: "))
# appleprice = int(input("Enter your price of apple: "))

# if(budget - appleprice > 80):
#     print("You can buy apple")
#     print("you have more than 80 rupees")
# elif(budget - appleprice > 50):
#     print("You can buy less apple")
#     print("you have more than 50 rupees")
# else:
#     print("you can't buy apple")
#     print("you have less than 50 rupees")


amount = int(input("Enter the amount you have: "))
networth = int(input("Enter your net worth: "))

if(amount >= 100):
    print("You can buy lambo")
    if(networth >= 1000):
        print("you can buy rolls royce also")
    else:
        print("You can't buy rolls royce")
else:
    print("you can't buy any car")