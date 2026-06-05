# Day - 50

#File methods

# f = open('basics of Python/day - 12/myfile.txt', 'r')  # Open a file for reading
# i = 0
# while True:
#     i += 1
#     line = f.readline()  # Read a single line from the file
#     if not line:  # If the line is empty, we have reached the end of the file
#         break
#     m1 = int(line.split(",")[0])
#     m2 = int(line.split(",")[1])
#     m3 = int(line.split(",")[2])
#     print(f"marks of student {i} in SS is: {m1*2}")
#     print(f"marks of student {i} in Maths is: {m2*2}")
#     print(f"marks of student {i} in English is: {m3*2}")
#     print(line)
# f.close()  # Close the file

f = open("basics of Python/day - 12/myfile.txt", "w")
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()