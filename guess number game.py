import random
target = random.randint(1,100)

while True :
    userChoice = input("Guess the number or type 'Quit' to exit :")
    if(userChoice.lower() == "quit"):
        break
    
    userChoice = int(userChoice)
    if(userChoice == target):
        print("Congratulation : You Guess the Correct Number...!!")
        break
    elif(userChoice < target):
        print("Your number was too small. Take a bigger guess..")
    else:
        print("Your number was too big. Take a smaller guess..")
        
print("-----GAME OVER-----")