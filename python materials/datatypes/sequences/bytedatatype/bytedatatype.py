# byte data type
# represents group of numbers like array
# can store values which are from 0 to 256
# cannot store negative numbers
# tocreate a data type
# we need to create a list
# the created list should be passed as a parameter to bytes function
# it is immutable which can not be modified or changes
# can iterate bytes values as uisng a for loop

# Example
a = [10,20,30,40,50,60,70,80]
# passing the created list as a parameter to the bytes
b = bytes(a)
# print the stored variable
print(b)
# print the type of the variable
print(type(b))

# Accessing the elements in byte array
print(b[0])
print(b[1])
print(b[2])
print(b[3])
print(b[4])
print(b[5])
print(b[6])
print(b[7])
# using for loop
for c in b:
    print(c)
    
# values must be in range of (0,256) 
# a = [10,20,300,25]
# b =bytes(a)
# print(b)
# print(type(b))

# immutable
# a = [10,20,1,25]
# b =bytes(a)
# b[0] = 30
# print(b)