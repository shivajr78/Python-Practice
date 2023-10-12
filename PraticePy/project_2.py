import random
randNumber = random.randint(1,10)
#print(randNumber)
userGuess = None #here prely defined userGuess for whileloop
guesses = 0
while(userGuess != randNumber):
    userGuess = int(input("Enter Your Guess Number: "))
    guesses += 1

    if(userGuess == randNumber):
        print("You Guessed it Right!")
    else:
        if(userGuess>randNumber):
            print("You Guessed it Wrong! Enter the Smaller Number")
        else:
            print("You Guessed it Wrong! Enter the Larger Number")
        

print(f"You guess the number in {guesses} guesses")
with open("hiscore.txt", "r") as f:
    hiscore = int(f.read())

if(guesses<hiscore):
    print("You have just broken the high score!")
    with open("hiscore.txt", "w") as f:
        f.write(str(guesses))