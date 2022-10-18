# Functions
# the line uses the keword def
# to inform python that you are defining function
# This function definition tells
# the python the name of the function and
# what kind of information the function needs to do its job
# The parentheses():  holds the information
# the indent line shows the or makes the body of the function
def greet_user():
    print("Hello World")
greet_user()    

# passing infdormation to a function
def greet_user(username):
    print("Hello "+ username.title()+"!")
greet_user('James')    