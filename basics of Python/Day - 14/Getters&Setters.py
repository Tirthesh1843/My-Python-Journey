#Day - 60

class myClass:
    def __init__(self, value):
        self.value = value
        
    def show(self):
        print(f"value is {self.value}")
        
    @property
    def Ten_value(self):
        return 10* self.value
    
    
    @property
    def Ten_value(self):
        return 10* self.value
    
    @Ten_value.setter
    def Ten_value(self, new_value):
        self.value = new_value/10
    
obj = myClass(10)
obj.Ten_value = 67
print (obj.Ten_value)
obj.show()