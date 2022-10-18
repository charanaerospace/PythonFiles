# class Employee:
#     def __init__(self, id):
#         self.id = id
#         print("The id is ", self.id)
# emp = Employee(1)        
# emp = Employee(2)        
# emp = Employee(3)        


# Class Name
class Employee:
    # Attributes Name
    def __init__(self, name, id):
        self.name = name
        self.id = id
    # Method Name
    def display(self):  
        print("The name is", self.name)
        print("The id is", self.id)
emp=Employee('a',1)
emp.display()        
