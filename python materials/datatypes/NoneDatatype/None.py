# None Data type 
# a)None Data type represents an object that does not contain any value
# b)if an object has no value than we can assign that object with None type
# Example
a = None
# prints  the variable
print(a)
# prints the type of the variables 
print(type(a))
# If any function and method is not returning anything then that method can  return none method
def balance():
    print("The minumim bal is")
    return 500
b = balance()
print(b)
print(type(b))