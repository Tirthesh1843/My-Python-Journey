#Day - 46

import os

# if os.path.exists("tirthesh.txt"):
#     print("File exists")
# else:
#     print("File does not exist")

folders = os.listdir("basics of Python")
print(folders)
try: # if the path is not a folder, it will throw an error
    for folder in folders:
        print(folder, end=": ")
        print(os.listdir("basics of Python/" + folder))
except:
    print("Not a folder")
    
if not os.path.exists("basics of Python/day - 12/folder1"):
    os.mkdir("basics of Python/day - 12/folder1")

for i in range(1, 6):
    os.mkdir("basics of Python/day - 12/folder1/test - " + str(i))
    