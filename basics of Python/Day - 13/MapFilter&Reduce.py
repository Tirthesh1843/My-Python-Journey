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

name = "Tirthesh"
print(name[0:4])
print(name[-4:-1])