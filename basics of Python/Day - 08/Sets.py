#Day - 31

#sets are unordered collection of unique items. They are defined using curly braces {} or the set() function. Sets do not allow duplicate elements and do not maintain any specific order.

Set = {2,4,2,1,11,1,2,5,4,3,2,1,2,3,4,5}
print(Set)
print(len(Set))
# print(Set[0]) error

info = {1,"Info", 3.14, (1,2,3), True, None}

empty_set = {} # this is a dictionary
print(type(empty_set)) # this is a dictionary not a set
null_set = set()
print(type(null_set)) # this is a set