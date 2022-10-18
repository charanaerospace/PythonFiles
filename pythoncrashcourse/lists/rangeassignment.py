# Use a for loop to print numbers from 1 to 20
for a in range(1,21):
    print(a)
    
# Use  for loop to print 1 to 100
for b in range(1,101):
    print(b)
#Make a list from 1 to 100 or 1 million print
# list = [1,2,3,4,5,6,7,8,9,10,11,12,13] 

# Make a list of odd numbers using the range function
odd_numbers = list(range(1,20,2))
print(odd_numbers)

a = [b**3 for b in range (1,15, 3)]
print(a)