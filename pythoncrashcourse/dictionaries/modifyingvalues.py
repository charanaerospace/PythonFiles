alien_0 = {}
# before modifying
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
# modifying the dictionary
alien_0['color'] = 'orange'
print(alien_0)

# example
alien_0 = {'x_position':0, 'y_position':25 , 'speed':'medium'}
print("The original x_position is"+str(alien_0['x_position']))
# condition
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 5
else:
    x_increment = 10
alien_0['x_position'] = alien_0['x_position'] +x_increment
print('new positoin is',str(alien_0['x_position']))           
