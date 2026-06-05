#Day - 47

# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning
# Your program should ask whether you want to code or decode a message and then ask for the message to code or decode. Finally, it should print the coded or decoded message.

import random

str1 = input("Enter the message: ")
words = str1.split(" ")
choice = input("enter 1 for coding and 2 for decoding: ")
coding  = True if choice == "1" else False
print("Coding")
# if coding:
#     new_str = ""
#     for word in words:
#         if len(word) >= 3:
#             new_str += "abc" + word[1:] + word[0] + "xyz" + " "
#         else:
#             new_str += word[::-1] + " "
#     print(new_str)
# else:
#     new_str = ""
#     for word in words:
#         if len(word) >= 3:
#             new_str += word[3:-3][-1] + word[3:-3][:-1] + " "
#         else:
#             new_str += word[::-1] + " "
#     print(new_str)

if coding:
    new_words = []
    for word in words:
        if len(word) >= 3:
            s1 = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3))
            s2 = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3))
            new_str = s1 + word[1:] + word[0] + s2
        else:
            new_str = word[::-1]
        new_words.append(new_str)
    print(" ".join(new_words))
else:
    new_words = []
    for word in words:
        if len(word) >= 3:
            new_str = word[3:-3]
            new_str = new_str[-1] + new_str[:-1]
        else:
            new_str = word[::-1]
        new_words.append(new_str)
    print(" ".join(new_words))