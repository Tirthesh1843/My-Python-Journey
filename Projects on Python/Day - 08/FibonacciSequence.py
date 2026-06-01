#fibonacci sequence

Fibonacci_sequence = int(input("How many terms do you need? "))
def fibonacci(n):
    if (n==1):
        return [0]
    elif (n == 2):
        return [0,1]
    else:
        sequence = fibonacci(n-1)
        sequence.append(sequence[-1] + sequence [-2])
        return sequence

print (fibonacci(Fibonacci_sequence))