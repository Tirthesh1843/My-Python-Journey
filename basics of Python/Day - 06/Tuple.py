#Day - 24
# tuple is a collection which is ordered and unchangeable. Allows duplicate members.

t = (1, 2, 3, 4, 5)
print (t, type(t))
print (len(t))
print (t[0]) #indexing starts from 0
print (t[1:4]) #slicing - returns elements from index 1 to 3

if 5 in t:
    print ("5 is present in the tuple")
else:
    print ("5 is not present in the tuple")

tup = t[1:4]
print (tup)
