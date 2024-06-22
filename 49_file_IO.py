# Open a file for reading

f = open('myfile49.txt', 'r')
# f = open('myfile49.txt') # r mode is default
text = f.read()
print(text)
f.close()

# modes in file 
# 1. read (r)   throws error if file don't exist
# 2. write (w)      create file if it is not exist
# 3. append (a)     create file if it is not exist
# 4. create (x)     create file and throw error if it already exist
# 5. rb / wb / ab is used to open jpg file , other than txt file 

# f = open("myfile49w.txt", 'w')
# f.write("hello, World!")
# f.close()


# f = open("myfile49w.txt", 'a')
# f.write("\nhello, World!")
# f.close()

# with open("myfile49w.txt", 'a') as f:
#     f.write("\nhey i am inside with")     # advantages: no need to close the file here
#     print(type(f))