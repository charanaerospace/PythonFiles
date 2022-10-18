class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age  = age
    def sit(self):
        print("The dog named"+self.name.title()+" is sitting there") 
        
    def roll(self):
        print("The dog named os"+self.name.title()+"is rolling over")      
        
my_dog =  Dog('Willey', 8)
print("My dog name is"+my_dog.name.title()+"!")         
print("My dog name is"+str(my_dog.age)+"years old")  
my_dog.sit()
my_dog.roll()       