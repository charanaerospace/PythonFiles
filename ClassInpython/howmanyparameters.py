# How many parameters can constructor has
# case1
class Employee:
    def __init__(self):
        print("const")
        print(self)
emp = Employee()  

# case2
class Employee:
    def __init__(self):
        self.id = 1
        print("self id is", self.id)
emp1=Employee()        
emp2=Employee()        
emp3=Employee()        