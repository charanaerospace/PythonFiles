# Number is a data type to store numeric values
# The object for the number will be created when the value is assigned to variable
# Types 
# 1.Int 
# 2.float
# 3.Complex
# Integer variable
# Int is a data type that returns ineteger type of values and also called as ints or integers
# Example
# variable assignemntoperators values
age = 28
# print var
print(age)
# type of var
print(type(age))

# Float variables
# floats are the values with decimal points divide the interger and fractional of numbers
salary = 3500.2589
# print var
print(salary)
# print type 
print(type(salary)) 

# Complex number
# The Complex is the number consisting of real and imaginary numbers  
a = 6+4j
# print var
print(a)
# print type of var
print(type(a))

# print(type(range(5)))

# aTuple = (1, 'Jhon', 1+3j)
# print(type(aTuple[2:3]))

# print(type({}) is set)

# x = 75
# def myfunc():
#     x = x + 1
#     print(x)

# myfunc()
# print(x)

x = 50
def fun1():
    x = 25
    print(x)
    
fun1()
print(x)

def func1():
    x = 50
    return x
func1()
print(x)

print(bool(0), bool(3.14159), bool(-3), bool(1.0+1j))

print(type([]) is list)