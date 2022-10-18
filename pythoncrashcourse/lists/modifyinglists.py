# Most lists are created will be dynamic you can add remove elements
# Changing the elements in the list
motor_cycle = ['ducati','honda','yamaha']
print(motor_cycle)
# replacing the values
motor_cycle[0] = 'KTM'
print(motor_cycle)
# Adding Elements To lists
# The simplest way to add a new element to a list is to append the item to the list
# the new element is added to the end of the list
motor_cycle.append('TomCat')
print(motor_cycle)
motor_cycle.append('Ducati')
print(motor_cycle)
# The append method makes it easy to build lists dynamically we can also start with empty ;ists
motorcycles = []
motorcycles.append('Ducati')
motorcycles.append('Honda')
motorcycles.append('KTM')
motorcycles.append('Tomcat')
print(motorcycles)
# The insert method allows to add a new element specifying the index of new elements
motorcycles.insert(4, 'Yamaha')
print(motorcycles)
# Removing elements from the lists
del motorcycles[4]
print(motorcycles)
# Pop method removes the last item  in a list
popped_motorcycles = motorcycles.pop()
print(popped_motorcycles)

last_owned = motorcycles.pop(0)
print("My last owned bike was "+last_owned.title()+"!")