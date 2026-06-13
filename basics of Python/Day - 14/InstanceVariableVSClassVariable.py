#Day - 66

class employee:
    company = "Google"
    
    def __init__(self, name):
        
        self.name = name
        self.raiseamount = 0.02
    
    def showDetails(self):
        print(f"name of the emploee is {self.name} and the raise amount in {self.company} is {self.raiseamount}")
    
emp1 = employee("Tirthesh")
emp1.raiseamount = 0.05
emp1.company = "Youtube"
emp1.showDetails()

emp2 = employee("Priya")
emp2.showDetails()