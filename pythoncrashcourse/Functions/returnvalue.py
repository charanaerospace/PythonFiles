# keyword functionname  parameters
# Here the function_name  name takes parameters a first and last name 
# The function combines the two names and adda a space between them them
# and stores the result in the full_name
# the value of  full_name is converted to title case and returned
# When you call this function that returns a value
# you must need a variable to store the return value
# the return value is stored in the variable Hello
def name(first_name, last_name):
    full_name = first_name +" "+last_name
    return full_name.title()

Hello = name('alfa', 'charlie')
print(Hello)
    
# Making Arguement Optional
# adding an extra parameter
def name(first_name, middle_name, last_name):
    full_name = first_name+" "+middle_name+" "+last_name
    return full_name.title()
code = name('Jimmy', 'lee', 'hendrix')
print(code)

# to make middile name optional
def name(first_name,last_name,middle_name=''):
    # apply ther conditions
    if middle_name:
        full_name = first_name+" "+middle_name+" "+ last_name
    else:
        full_name = first_name+" "+last_name 
    return full_name.title()
lift =name('jimi', 'hendrix')
print(lift)
lift=name('jimi', 'hendrix', 'lee')
print(lift)        