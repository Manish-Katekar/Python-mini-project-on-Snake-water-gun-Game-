'''
Snake Water Gun is a Two-player game in which one is computer player who randomly chooses any of the three forms i.e. snake, water, gun 
and another player is user who chooses their form from given three forms by entering the input. Winner decided as follows-  


Snake vs. Water: Snake drinks the water hence wins.
Water vs. Gun: The gun will drown in water, hence win for water
Gun vs. Snake: Gun will kill the snake and win.
In situations where both players choose the same object, the result will be a draw.
'''

import random

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'g':
            return True
        elif you == 'w':
            return False
    elif comp == 'g':
        if you == 'w':
            return True
        elif you == 's':
            return False
    elif comp == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False

print("Comp Turn : Snake(s) Water(w) or Gun(g) ")


rand_no = random.randint(1,3)


if rand_no == 1:
    comp = 's'
elif rand_no == 2:
    comp = 'g'
elif rand_no == 3:
    comp = 'w'

you = input("Your Turn : Snake(s) Water(w) or Gun(g) ")
a = gameWin(comp, you)

print(f"computer choice {comp}")
print(f"your choice {you}")

if a == None:
    print("The game is Tie")
elif a:
    print("you won the game")
else:
    print("you lost the game")




        
