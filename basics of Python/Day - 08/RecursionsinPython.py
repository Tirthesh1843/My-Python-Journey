# Day - 30

# factorial (7) = 7*6*5*4*3*2*1
# factorial (0) = 1
# factorial (1) = 1
# factorial (n) = n*factorial(n-1)

factorial_number = int(input("Enter the number for which you want to get factorial: "))

def factorial (n):
    if (n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
print (factorial(factorial_number))