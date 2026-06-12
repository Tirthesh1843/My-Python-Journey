#Day - 62

#Types of access modifiers in python
#1. Public
#2. Private
#3. Protected

class Employee:
    def __init__(self):
        self.name = "Harry" #public
        self._age = 23 #protected
        self.__salary = 20000 #private

a = Employee ()
print(a.name)
print(a._age)
# print(a.__salary) this will give error
print(a._Employee__salary) #this will work  