#Day - 32

cities = {"Delhi", "Mumbai", "Bangalore", "Chennai", "Kolkata"}
cities2 = {"Hyderabad", "Pune", "Bangalore", "Ahmedabad", "Lucknow", "Chennai"}

cities3 =  cities.union(cities2) # union of two sets 
print(cities3)

cities4 = cities.intersection(cities2) # intersection of two sets
print(cities4)

cities.intersection_update(cities2) # updates the original set with the intersection of two sets
print(cities)

cities5 = cities.symmetric_difference(cities2) # difference of two sets
print(cities5)

print (cities.isdisjoint(cities2)) # checks if two sets are disjoint (no common elements)

print(cities.issubset(cities4)) # checks if cities is a subset of cities2

# cities.remove("Delhi") # removes an element from the set, raises an error if the element is not found
# print(cities)

cities.discard("Delhi") # removes an element from the set, does not raise an error if the element is not found
print(cities)