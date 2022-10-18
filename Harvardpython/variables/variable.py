# Variables
# variablename   assignmentoperator  values to be stored
# x = input("Enter your name")
# print("Hello", x)

# method 1
# x = input("Enter your name")
# print(x)

# Ask user to enter name
# name = input("ENter your name")
# # say hello to users
# print("Hello," + name)

# using the strings and parameters

# name = input("Enter the name you want to enter")
# print("hello,")
# print(name)

# name = input("Enter the name you want to enter")
# print("hello," , end="")
# print(name)

# name = input("Enter the name you want to enter")
# print("hello," , end="\n")
# print(name)
# format strings
# name = input("Whats your name?")
# print(f"Hello, {name}")
# stripping
name = input("Whats your name?")
name = name.strip()
print(f"Hello, {name}")
# capitalize
name = input("Whats your name?")
name = name.strip()
name = name.title()
print(f"Hello, {name}")
name = input("Whats your name?").strip().title()
print(f"Hello, {name}")