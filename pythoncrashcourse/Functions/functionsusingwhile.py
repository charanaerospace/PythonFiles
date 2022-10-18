def name(first_name, last_name):
    full_name = first_name+" "+last_name
    return full_name.title()
while True:
    print("\n Enter Name")
    f_name = input("Enter your first name")
    l_name = input("Enter your last name")
    
code = name('f_name','l_name')
print("\nHello, "+ code +"!")