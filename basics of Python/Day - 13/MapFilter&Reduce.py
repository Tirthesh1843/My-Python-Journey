#Day - 53

def cube(x):
    return x ** 3

print(cube(3))

l = [1, 2, 4, 6, 4, 5]
# newl = []
# for item in l:
#     newl.append(cube(item))
# print(newl)

newl = list(map(cube, l)) #
print (l, " -> ", newl)

#filter
def filter_function(a):
    return a>4

newnewl = filter(filter_function, l)
print (l, " -> ", list(newnewl))

#reduce
from functools import reduce
newnewnewl = reduce(lambda x, y: x+y, l)
print (l, " -> ", newnewnewl)

def mysum(x,y):
    return(x+y)

sum = reduce(mysum, l)