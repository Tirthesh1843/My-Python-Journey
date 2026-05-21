#Day - 11

"""Strings are a sequence of characters. They are used to store text data. They are immutable, which means that they cannot be changed after they are created."""

Name = "Tirthesh"
Friend = "Karan"
AnotherFriend = "Premal"

print (Name + " is a friend of " + Friend)
print (Friend + " is a friend of " + AnotherFriend)

print (Name[0]) #T
# print (Name[10]) IndexError: string index out of range

for i in Name:
    print (i, end = " ") #T i r t h e s h
    
#Day - 12
#String slicing is the process of extracting a portion of a string. It is done using the slice operator [:]. The syntax for slicing is: string[start:end:step]

Fruit = "Mango"
fruitlen = len(Fruit)
print (fruitlen) #5
print (Fruit[0:3]) #Man
print (Fruit[1:]) #ango
print (Fruit[:3]) #Man
print (Fruit[-1:])
# print (Fruit[-1:len(Fruit)]) #error
print (Fruit[-3:-1]) #ng

# Quiz: What will be the output of the following code?
nm = "Harry"
print (nm[-4:-2]) #Hry