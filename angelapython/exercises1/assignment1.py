print("Welcome to the Game")
name =input("Enter your name")
age = int(input("Enter the age"))
print("Hello  " +name+ "is " + str(age)+" years old")
health = 15
if age >= 18:
    print("You are eligible to play")  
    want_to_start = input("Do you want to play")
    if want_to_start == 'yes':
        print("Let's Play")
    left_or_right = input("ENter left or right")
    if left_or_right == 'left':
        ans = input("reched the lake path how would you move around/across")
        if ans == 'around':
            print("Reached the target safely")
        elif ans == 'across':
            print("You swam and lost heath of 3 point")
        else:
            print("Kidnapped")                                   
    else:
        print("See you soon")                    
else:
    print("Not eligible to play")    