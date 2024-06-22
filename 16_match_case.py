x = int(input("Enter a number to match: "))
# x is the variable to match

match x:
    case 0:
        print("x is zero")

    # case with if-condition
    case 4 if x % 2 == 0:
        print("x % 2 == 0 and case is 4")

    # Empty case with if-condition
    # case _ if x < 10:
    #     print("x is < 10")
    
    case _ if x != 90:
        print(x, "is not 90")

    # default case ( will only matched when if the above cases were not matched)
    case _:
        print(x)
        

