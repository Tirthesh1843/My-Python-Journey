#Day - 22

l = [1, 2, 3, 4, 5]
# print (l)
# print (type(l))

if 4 in l:
  print ("4 is present in the list")
  print ("Index of 4 is:", l.index(4))
else:
  print ("4 is not present in the list")
  l.append(4) #append is used to add an element at the end of the list

if "TIR" in "TIRTHEsh":
  print ("TIR is present in the string")
else:
  print ("TIR is not present in the string")
  
print (l)
print (l[0]) #indexing starts from 0
print (l[1:4]) #slicing - returns elements from index 1 to 3
print (l[::2]) 