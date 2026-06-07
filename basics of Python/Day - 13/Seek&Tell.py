with open ('basics of Python/day - 13/file.txt', 'r') as f:  # Open a file for reading using the with statement (this will automatically close the file after the block is executed)
    print (type(f))  # Print the type of the file object (should be <class '_io.TextIOWrapper'>)
    # move the file pointer to the 10th byte from the beginning of the file
    f.seek(10)
    
    # read the next 5 bytes from the file
    print(f.tell())  # Print the current position of the file pointer (should be 10)
    data = f.read(5)
    print(data)
    
with open ('basics of Python/day - 13/file.txt', 'w') as f:  # Open the same file for writing
    f.write("Hello, World!")
    f.truncate(5)  # Truncate the file to 5 bytes (this will remove everything after the first 5 bytes)

with open ('basics of Python/day - 13/file.txt', 'r') as f:  # Open the file again for reading
    print( f.read() )  # Print the contents of the file (should be "Hello")