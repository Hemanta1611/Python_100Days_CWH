# f = open('myfile50.txt', 'r')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)


# f = open('myfile50b.txt', 'r')
# i = 0
# while True:
#     i = i + 1
#     line = f.readline()
#     if not line:
#         break
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]
#     print(f"Marks of Student{i} in Math is: {m1}")
#     print(f"Marks of Student{i} in Odia is: {m2}")
#     print(f"Marks of Student{i} in SST is: {m3}")

# f = open('myfile50w.txt', 'w')
# lines = ['line 1\n', 'line 2\n', 'line 3\n']
# f.writelines(lines)
# f.close

f = open('myfile50w.txt', 'w')
lines = ['line 1', 'line 2', 'line 3']
for line in lines:
    f.write(line + "\n")
f.close
