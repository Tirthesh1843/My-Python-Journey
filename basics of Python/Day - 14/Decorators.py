# Day - 59

def greet(fx):
    def mdf(*args, **kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("thank you for using our service")
    return mdf

@greet
def hello():
    print ("hello World")

@greet
def add(a,b):
    print (a+b)

# greet(hello)()

hello()
add(5,13)