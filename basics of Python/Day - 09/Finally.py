#Day - 37
def function():
    list1 = [1,2,3,4,5]
    try:
        a = int(input("Enter an index: "))
        print (f"The value at index {a} is {list1[a]}")
        return 1
    except:
        print ("An error occurred. Please check the index and try again.")
        return 0

    finally:
        print ("This block will always be executed, regardless of whether an exception occurred or not.")
    print ("This line will not be executed.")

x = function()
print (x)