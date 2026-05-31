#Day - 025
# operators in tuple are same as list but we cannot change the elements of a tuple once it is created. We can only access the elements of a tuple using indexing and slicing. We can also check if an element is present in a tuple using the 'in' keyword.

Country = ("India", "USA", "UK", "Australia", "Canada")

temp = list(Country) #converting tuple to list
temp[0] = "China" #changing the first element of the list
temp.pop(3)
country = tuple(temp) #converting list back to tuple
print (country)
