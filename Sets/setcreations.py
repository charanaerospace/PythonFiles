# Using the braces
days = {'m','t','w','t','f','s','s'}
print(days)
print(type(days))

# Using the set method
days = (['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
print(days)
print(type(days))
# using the for loop
for day in days:
    print(day)
    
# Empty set
a = {}
print(type(a))

#Adding an Element into the set
a = {1,2,3,4,5,6,7,8,9,10,11,12}
print(a)
a.add(14)
print(a)

# Update elements in a set
x = {1,2,3}
y = {1,2,3,4}
x.update(y)
print(x)
# 9885358577  
#Removing an Element into the set
a = {1,2,3,4,5,6,7,8,9,10,11,12}
print(a)
a.remove(10)
print(a)

# clear method
days = {'m','t','w','t','f','s','s'}
days.clear()
print(days)

# Sets union
a = {1,2,3}
b = {2,3,4}
print(a | b)
# Intersection
print(a & b)
# Difference
x = {1,2,3}
y = {2,3,4}
print(x ^ y)

x = {1,2,3}
y = {2,3,4}
print(x.issubset(y))
# x = {1,2,3}
# y = {2,3,4}
# print(x.isin(y))

# x = {1,2,3}
# y = {2,3,4}
# print(x.is_in(y))

x = {1,2,3}
y = {2,3,4}
print(x in y)