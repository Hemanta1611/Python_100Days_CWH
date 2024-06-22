a = input("Enter the number: ")
print(f"Multiplication table of {a} is: ")

# if we take input as not a number than it will throw error and next line of code also interuppt i.e. it will also not execute
# to execute next code / program , we use exceptional handling

try:
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a)*i}")
# except:
#     print("Invalid Input By User.. ")
except Exception as e:
    print(e)



# print()
# print("Some important lines of Codes")
# print("End of Program")
# print()

# try:
#     n = int(input("Enter a number: ")) # it will show error when we take input other than integer type
#     print("The number is: {n}")
# except Exception as xyz:
#     print(xyz)
# print()



# try:
#     num = int(input("Enter the index: "))
#     lis = [6, 3]
#     print(lis[num])
# except ValueError:
#     print("Number entered is not an integer.")
# except IndexError:
#     print("Index Error.")

