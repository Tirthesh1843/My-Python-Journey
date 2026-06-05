#Day - 49

#File I/O
#File handling in Python is done using the built-in open() function, which allows you to read from and write to files. Here are some common operations for file I/O in Python:

#1. Opening a file:

f = open('basics of Python/day - 12/myfile.txt', 'r')  # Open a file for reading

# 2. Reading from a file:
content = f.read()  # Read the entire content of the file
print(content)
# f.write("This is a new line.\n")  This will throw an error because the file is opened in read mode
f.close()  # Close the file

#3. Writing to a file:
# f = open('myfile.txt', 'w')  # Open a file for writing (this will overwrite the file if it already exists)
# # f.read()
# f.write("Hello, World!\n")  # Write a string to the file
# f.close()

#4. Appending to a file:
f = open('basics of Python/day - 12/myfile.txt', 'a')  # Open a file for appending (this will add to the end of the file if it already exists)
f.write("This is an appended line.\n")  # Append a string to the file
f.close()

#5. Reading and writing to a file:
f = open('basics of Python/day - 12/myfile.txt', 'r+')  # Open a file for reading and writing
content = f.read()  # Read the entire content of the file
print(content)
f.write("This is a new line.\n")  # Append a string to the file
f.close()

#6. with statement for file handling:
with open('basics of Python/day - 12/myfile.txt', 'a') as f:  # Open a file for appending using the with statement (this will automatically close the file after the block is executed)
    f.write("This is an appended line using with statement.\n")  # Append a string to the file

#6. binary mode:
# f = open('myfile.txt', 'rb')  # Open a file for reading in binary mode, pdf/image files are usually opened in binary mode
# content = f.read()  # Read the entire content of the file as bytes
# print(content)
# f.close()

#7. creating a file if it doesn't exist:
f = open('basics of Python/day - 12/newfile.txt', 'w')  # Open a file for writing (this will create the file if it doesn't exist)
f.write("This is a new file.\n")  # Write a string to the file
f.close()
f = open('basics of Python/day - 12/newfile.txt', 'r')  # Open the newly created file for reading
content = f.read()  # Read the entire content of the file
print(content)
f.close()

#8. deleting a file:
import os
os.remove('basics of Python/day - 12/newfile.txt')  # This will delete the file newfile.txt from the directory