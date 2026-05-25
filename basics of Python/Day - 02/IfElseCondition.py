#Day - 14
A = int(input("Enter Your Age: "))
print ("Your Age is: ", A)
if (A>18):
  print ("You are Eligible for Voting")
  print ("yes")
else:    
  print ("You are Eligible for Voting")
  print ("no")
  print ("Thank You")
  
#conditional operators >, <, >=, <=, ==, !=

Budget = int(input("Enter Your Budget: "))
applePrice = 100
if (Budget>apple):
  print ("You can buy Apple")
else:  
  print ("You cannot buy Apple")
  
# else if lader

num = int(input("Enter a Number: "))
if (num<0):
  print ("Negative Number")
elif (num>0):
  if num<=10:
    print ("Positive Number and less than or equal to 10")
  elif num>10 and num<=20: 
    print ("Positive Number and greater than 10 and less than or equal to 20")
  else:
    print ("Positive Number and greater than 20")
else:
  print ("number is Zero")