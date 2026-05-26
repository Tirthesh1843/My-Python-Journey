#guess the number game wit help of while loop and random module
import random

y = random.randint(1,5000)
X = int(input("guess a number between 1 and 5000: "))
while(X != y):
  if X < y:
    print ("Too low")
  else:
    print ("Too high")
  X = int(input("guess a number between 1 and 5000: "))
print ("Congratulations! you guessed the number")