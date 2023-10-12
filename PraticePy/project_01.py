import random


def gameWin(computer, you): #game func for camparing comp and your select option
    if computer == you:  #Value are than tie
        return None

    #check all possibilities when computer choose 's'
    elif computer == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True

    #check all possibilities when computer choose 'w'
    elif computer == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True

    #check all possibilities when computer choose 'g'
    elif computer == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True


print("Computer turn: water(w) snake(s) or gun(g)?")
randNO = random.randint(1, 3) #here computer choosing the option 
if randNO == 1:      #random 1,2,3 are linking with option
    computer = 's'
elif randNO == 2:
    computer = 'w'
elif randNO == 3:
    computer = 'g'

you = input("Your turn: snake(s) water(w) or gun(g)??\n")
a = gameWin(computer, you)

#Printing what you and computer had choosen
print(f"Comp Choose {computer}")
print(f"You Choose {you}")

if a == None:
    print("The Game is Tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")
