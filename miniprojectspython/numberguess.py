import random
number_range = input("Enter the number: ")
if number_range.isdigit():
    number_range = int(number_range)
    
    if number_range <= 0:
        print("Enter number bigger than zero")
        quit()
else:
    print('Type a number next time') 
    quit()       
random_number = random.randint(0, number_range)
guess  = 0
while True:
    guess += 1
    user_guess  = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        
    else:
        print('Type a number next time') 
        continue
    
    if user_guess == random_number:
        print("You got it")
        break
    elif user_guess > random_number:
        print('you are above the number')
    else:
        print('you are below the number')    
print("You got in", guess,'guesses')     
# print(random_number) 