#Day - 38

# Custom error handling in Python

print ("Welcome to the custom error handling example.")

a =int(input("Enter a number between 1 and 10: "))

if a < 1 or a > 10:
    raise ValueError("The number must be between 1 and 10.")
