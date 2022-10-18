# class name
class Dog:
    # attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    #Methods
    def sit(self):
        print("The dog name"+self.name+" is there sitting")
     
    def  roll(self):
        print("the dog named is "+self.name.title()+"is stiing over there "+ str(self.age) +"years") 
        
dog =Dog('snoopy', 6)
dog.sit()
dog.roll()             