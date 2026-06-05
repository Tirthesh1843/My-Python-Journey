#Day - 48

a = 10 # a is a global variable and can be accessed anywhere in the program
def func1():
    a = 20
    b = 30 # b is a local variable in func1 and cannot be accessed outside of it
    print("Inside func1: ", a, b)
def func2():
    print("Inside func2: ", a)
func1()
func2()
# print("Outside: ", b): this will throw an error because b is a local variable in func1 and cannot be accessed outside of it
print("Outside: ", a)

def func3():
    global a # this will tell the program that we want to use the global variable a and not create a new local variable a
    a = 40 # this will change the value of the global variable a to 40
    print("Inside func3: ", a)
func3()
print("Outside: ", a) # this will print 40 because we changed the value of the global variable a in func3