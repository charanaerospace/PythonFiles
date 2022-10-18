# class Name
class User:
    # attributes
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    #Methods
    def describe_user(self):
        print("The user name is "+self.first_name.title()) 
        print("The user name is "+self.last_name.title()) 
    
    def greet_user(self):
        print("Welcome to " +self.first_name.title()+" kiosk")    
        print("Welcome to " +self.last_name.title()+" kiosk")  

user = User('alfa', 'beta')
user.first_name
user.last_name
user.describe_user()
user.greet_user()          