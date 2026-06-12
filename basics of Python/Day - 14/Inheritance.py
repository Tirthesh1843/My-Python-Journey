#Day - 61

class employee:
    def __init__(self, name,  id):
        self.name = name
        self.id = id
    
    def showdetails(self):
        print(f"{self.name} has id {self.id}") #print(self.name, self.id)

class Programmer(employee):
    def showlanguage(self):
        print(f"{self.name} is a Programmer. and he uses Python")

e1 = employee("Tirthesh", 23)
e1.showdetails()
e2 = Programmer("Priya", 24)
e2.showdetails()
e2.showlanguage()