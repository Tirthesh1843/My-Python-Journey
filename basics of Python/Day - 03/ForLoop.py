#Day - 17

# name = "Tirthesh"
# for i in name:
#   print (i, end = ",")

Colors = ["Red", "Green", "Blue", "Yellow"]
for i in Colors:
  print (i)
  for X in i:
    print (X)

for i in range(1, 11, 2):
  print (i)

#reverse string using for loop
string = input("Enter a string: ")
i =""
for X in string:
  i = X+i
print (i)