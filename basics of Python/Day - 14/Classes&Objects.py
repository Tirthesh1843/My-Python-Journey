#Day - 57

class Person:
    name = "Tirthesh"
    age = 23
    occupation = "web developer"
    def info(self):
        print (f"{self.name} is {self.age} years old & Works as {self.occupation}.")

a = Person()
a.name = "Premal"
a.occupation = "Toy Seller"
a.age = 26
# print (a.name)
# print (a.age)
# print (a.occupation)
a.info()

b = Person()
# print (b.name)
# print (b.age)
# print (b.occupation)

b.info()