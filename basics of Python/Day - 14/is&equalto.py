#is vs ==

# x = 5
# y = 5

x = [1,2,3]
y = [1,2,3]

print(x == y) #exact location of object in memory (returs true)
print(x is y) #value (returns false if mutable objects are used)