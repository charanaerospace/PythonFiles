# class Name
class Restarurant:
    # Attributes
    def __init__(self, name, cusine_type):
        self.name = name
        self.cusine_type = cusine_type
    # Method
    def describe_restaurant(self):
        print("The name of the restaurant"+self.name.title()) 
        print("The type of the cusine is" +self.cusine_type)
        
    def open_resturant(self):
        print("the restaurant named"+self.name.title()+"is now open")    
        
restaurant =Restarurant('Nawabs','Asian')
restaurant.describe_restaurant()   
restaurant.open_resturant()     
        