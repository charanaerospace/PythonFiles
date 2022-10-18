def human(first_name , last_name): 
    person = {'first':first_name , 'last': last_name}
    return person
code = human('Elvis', 'presily')
print(code)


def human(first_name,last_name,age=''):
    person ={'first': first_name, 'last':last_name} 
    if age:
        person['age'] = age
    return age
code_1 = human('Elvis','Presly', age=25) 
print(code_1)       