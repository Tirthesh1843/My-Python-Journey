#Find Common Elements in Two Lists
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]
common_elements = []
for i in list1:
    if i in list2:
        common_elements.append(i)
print(common_elements)
# here it should return [2,4] not [2,2,4,4] because 2 and 4 are common in both lists but they are repeated in list1 and list2 respectively. So we can use set to remove duplicates from the lists before finding common elements. without using set.
list1 = [1, 2, 2, 3, 4, 4, 5]
list2 = [2, 2, 4, 6, 8]
common_elements = []
for i in list1:
    if i in list2 and i not in common_elements:
        common_elements.append(i)
print(common_elements)


numbers = [12, 12, 45, 23, 67, 45, 89, 12, 90, 23]

unique_numbers = []

for i in numbers:
    count = 0

    for j in numbers:
        if i == j:
            count += 1

    if count == 1:
        unique_numbers.append(i)

print(unique_numbers)