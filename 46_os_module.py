"""
The os module in Python is a built-in library that provides functions for interacting with the 
operating system. It allows you to perform a wide variety of tasks, such as reading aand writing
files, interacting with the file system, and running system commands.
"""

import os

if(not os.path.exists("Data")):
    os.mkdir("Data")
    

for i in range(1, 101):
    os.mkdir(f"Data/Day{i}")
    # os.rename(f"Data/Day{i}", f"Data/Tutorial {i}")

folders = os.listdir("Data")
print(folders)

# to check file inside the folders 
for folder in folders:
    print(folder, os.listdir(f"Data/{folder}"))


#   ********************************    #
    # explore OS module of pyhton #
#   ********************************    #



# Open the file in read-only mode
# f = os.open("myfile.txt", os.O_RDONLY)

# Raad the content of the file
# contents = os.read(f, 1024)

# Close the file
# os.close

# Open the file in write-only mode
# f = os.open("myfile.txt", os.O_WRONLY)


