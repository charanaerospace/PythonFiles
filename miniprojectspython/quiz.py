print("Welcome to My Quiz")
playing = input("Enter yes or no to play ? ") 

if playing.lower() != "yes":
    quit()
print("Let's Play")
score = 0

answer = input('What deos ram stand for? \n')
if answer.lower() == "random access memory":
         print("Correct Answer")
         score += 1
else:
    print("Wrong Answer")            
    
answer = input(' What deos GPU Stands for ? \n')
if answer.lower() == "graphics processing unit":
         print("Correct Answer")
         score += 1

else:
    print("Wrong Answer")      
    
answer = input(' What deos PSU Sands for ? \n')
if answer.lower() == "power supply unit":
         print("Correct Answer")
         score += 1
else:
    print("Wrong Answer")       
    
print("You got a score of  " +  str(score)  + " questions correctly")       
print("You got a score of  " +  str((score/4) * 100) + "%.")       