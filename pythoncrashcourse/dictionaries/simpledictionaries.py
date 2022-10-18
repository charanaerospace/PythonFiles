# dictionary in python is called a combination of key value pairs
# Each key is connected to a value and
# use a key to access the value associated with it
# key value can be number or list or string or other dictionaries
# dictionaries are wrapped in braces
# a key vaue pair is a set f  values associated with each other
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
# Accessing Values in dictionaries
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("Congratulations you just earned"+str(new_points)+"points")