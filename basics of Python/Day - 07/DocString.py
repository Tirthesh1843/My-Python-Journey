#Day - 029

#python docstring are used to describe the purpose of a function, class, or module. They are enclosed in triple quotes (""" """) and can span multiple lines. Docstrings provide a convenient way to document your code and make it easier for others (or yourself in the future) to understand what a particular piece of code does.

def square (n):
    '''Takes a number n and returns its square.'''
    print(n**2)
square(5)
print(square.__doc__)