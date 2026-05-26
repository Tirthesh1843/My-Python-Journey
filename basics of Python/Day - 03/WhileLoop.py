#Day - 18
import random

i = 5
while i > 0:
  print (i)
  i -= 1

i = 0
while i < 5:
  print (i)
  i += 1

y = random.randint(1,5000)
X = int(input("guess a number between 1 and 5000: "))
while(X != y):
  if X < y:
    print ("Too low")
  else:
    print ("Too high")
  X = int(input("guess a number between 1 and 5000: "))
print ("Congratulations! you guessed the number")