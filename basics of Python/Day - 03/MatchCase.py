X = int(input("Enter a number: "))
match X:
  case 1:
    print ("You entered 1")
  case 2:
    print ("You entered 2")
  case 3:
    print ("You entered 3")
  case _ if X > 3:
    print ("You entered a number greater than 3"  )
  case _:
    print ("You entered 0 or a negative number")

# when int not in input it will throw an error in case with if > can not be used because it is not an int but a string.