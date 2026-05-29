#Day - 21
def average (a = 9,b = 1):
  print ("average is:", (a+b)/2)
average (1, 4) 
average(6)

def three (a,b,c=1):
  print ("average is:", (a+b+c)/3)
three (1, 2)
# three (1, , 3) #TypeError: three() missing 1 required positional argument: 'b'

def four (*numbers):
  sum = 0
  for i in numbers:
    sum = sum + i
  # print ("average is:", sum/len(numbers))
  return sum/len(numbers) #return is used to return a value from a function and exit the function.

c = four (1, 2, 3, 4)
print (c)