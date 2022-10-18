# bytearray
# it is same as byte data type
# it is mutable
# Creation of byte array
# Create a list
# pass the list to function bytearray()
# iterate bytearray values using the loop

a = [10,20,30,40,50,60,71]
# passing the list to byte array  using a variable to store
b = bytearray(a)
print(b)
print(type(b))

# Accessing the bte array
print(b[0])
print(b[1])
print(b[2])
print(b[3])
print(b[4])
print(b[5])
print(b[6])
# using for loop
for c in b:
    print(c)
    
# byte array is mutable
a = [10,20,30,40,50,60,71]
# passing the list to byte array  using a variable to store
b = bytearray(a)
# before assigning new variable
print(b)
# after assigning nw variable
b[0] = 80
print(b)