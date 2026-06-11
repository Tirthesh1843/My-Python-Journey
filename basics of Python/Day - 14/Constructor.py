class person:
    name = "Tirthesh"
    occupation = "AI developer"
    
    def __init__(self, n, o):
        print ("Hey i'm a person")
        self.name = n
        self.occupation = o
    def info(self):
        
        print(f"{self.name} Works as {self.occupation}.")
        
a =person("Priya", "Doctor")
b = person("Tirthesh", "AI Developer")
# a.name = "Priya"
# a.occupation = "Doctor"
# a.info()
# c = person()
a.info()
b.info()