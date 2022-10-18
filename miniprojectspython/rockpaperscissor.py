import random
# declaring variables
user_win = 0
computer_win = 0
# list declarations
choice = ['Rock','Paper','Scissor']
# Using the condition 1
while True:
    user_input = input("Enter  Rock or Paper or Scissor or q to quit")
    # condition 1
    if user_input == 'q':
        break
    # condition 2
    if user_input not in choice:
        continue
    
    random_number = random.randint(0, 2)
    computer_pick = choice[random_number]
    print("computer pick is", computer_pick + ".")
# condition 3
    if user_input == 'rock' and computer_pick == 'scissor':
        print("you won")
        user_win += 1
        
    elif user_input == 'paper' and computer_pick == 'rock':
        print("you won")
        user_win += 1
        
    elif user_input == 'scissor' and computer_pick == 'paper':
        print("you won")
        user_win += 1
    else:
        print("you lost")
        computer_win += 1


print("You won", user_win, 'times')
print("Computer won", computer_win, 'times')
print("Good Bye")               
           
     
