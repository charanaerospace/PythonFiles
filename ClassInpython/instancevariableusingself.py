# class Name
class Employee:
    # attributes
    def __init__(self):
        self.eno =1
        self.name = 'Abc'
        self.salary = 2500
e = Employee()
print("Employee id is", e.eno)        
print("Employee name is", e.name)        
print("Employee salary is", e.salary)  
print(e.__dict__)      
print(e.__dir__)     