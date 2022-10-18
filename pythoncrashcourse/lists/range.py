# Range function is easy to generate a series of numbers
# loop value  range(parameters)
for value in range(1,5):
    print(value)

for a in range(1,11):
    print(a)    
    
# Use range to make list of numbers     
numbers = list(range(1,15))
print(numbers)

# even numbers
even_numbers = list(range(2,11,2))
print(even_numbers)

# square of numbers
squares = []
for a in range(1,11):
    b = a **2
    squares.append(b)
print(squares)    

squares = []
for a in range(1,11):
    squares.append(a **2)
print(squares)    

squares = [a**2 for a in range(1,11)]
print(squares)