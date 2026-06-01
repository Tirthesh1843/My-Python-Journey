#Day - 36

A = input("Enter a number: ")
print (f"Multiplication table of {A} is:")
try:
    for i in range(1,11):
        print (f"{int(A)} X {i+1} = {int(A) * (i+1)}")
except Exception as e:
    print (e)

print ("This line will be executed regardless of whether an exception occurred or not.")