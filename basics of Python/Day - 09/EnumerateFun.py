#Day - 42

# Enumerate function in Python

marks = [90, 80, 70, 60]
# index = 0
# for mark in marks:
#     print (mark)
#     if (index == 0):
#         print ("Tirthesh awesome")
#     index += 1

for index, mark in enumerate(marks):
    print (mark)
    if (index == 0):
        print ("Tirthesh awesome")