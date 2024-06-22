# try:
#     num = int(input("Enter an integer: "))
#     lis = [6, 3]
#     print(lis[num])
# except ValueError:
#     print("Number entered is not an integer.")
# except IndexError:
#     print("Index Error.")
# except:
#     print("Some error occurred")
# finally:
#     print("I am alsways executed")
# print("I am always excuteeddd")


# finally keyword have no work if we write normally by just directly printing print() statememnt
# finally keyword works in a funtion 


def func():
    try:
        l = [1, 5, 6, 7]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("some error occurred")
        return 0
    finally:
        print("I am always executed")
    print("I am always executedddd but i am not excutable in function if it is not meet the condition")

x = func()
print(x)

