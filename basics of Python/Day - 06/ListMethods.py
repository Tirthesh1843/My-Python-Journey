# Day - 23

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
l = [11, 21, 13, 41, 15]
print (l)
l.append(0.6) #append is used to add an element at the end of the list
l.sort(reverse = True) #sort is used to sort the list in ascending order, reverse=True sorts in descending order
l.reverse() #reverse is used to reverse the list
print (l.index(13)) #index is used to find the index of the first occurrence of an element in the list
print (l.count(11)) #count is used to count the number of occurrences of an element in the list
m = l
m[0] = 0
print (l) #both l and m are pointing to the same list in memory, so changes in m will reflect in l
l.insert(2, 100) #insert is used to insert an element at a specific index in the list
print (l) 
t = [100,350,123]
k = l+t+[0] #k is a new list that contains the elements of l and t
l.extend(t) #extend is used to add elements of another list to the end of the list
print (k)
print (l)
print (l.pop(2)) #pop is used to remove an element from the list
print (l)
l.remove(100) #remove is used to remove an element from the list
print (l)
l.copy() #copy is used to create a copy of the list
l.clear() #clear is used to remove all elements from the list