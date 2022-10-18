# variables
from re import A


x = 5
y = 'j'
print(x)
print(type(x))
print(y)
print(type(y))
#Casting
a = str(3)
print(a)
b = int(a)
print(b)
c = float(b)
print(c)

'''
x = 5
y = 'j'
print(x)
print(type(x))
print(y)
print(type(y))
'''

# Variable naming
myvar = 'Jhon'
my_var = 'Jhon'
_my_var = 'Jhon'
myvar = 'Jhon'
MYVAR = 'j'
myvar2 = 'j'    
# Multiword variables
# CamelCase
myName = 'ABC'
print(myName)
# Pascal case variables
MyName = 'ABC'
print(myName)
# Snake case variables
my_name = 'abc'
print(my_name)

# Mulitple variable
x, y, z = 'Orange','Banana','Red'
print(x)
print(y)
print(z)
# assigning same value to multiple variables
x=y=z='Apple'
print(x)
print(y)
print(z)
# Unpacking Collection
fruits = ['a','b','c']
j, k, l = fruits
print(j)
print(k)
print(l)

# global variable
a = 'Hello'
def b():
    print('Hello' + a)
b()    
# local variable
a = 'Hello'
def b():
    a = 'Awsome'
    print('Hello' + a)
b()    
print('Hello' + a)
