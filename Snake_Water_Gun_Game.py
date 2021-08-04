import random


# Snake Water Gun or Rock paper Scissors  
def gameWin(comp, p2):
#   If two values are equal , Declare a tie
    if comp == p2:
        return None
    #Check For all Posibilities when computer choose s
    elif comp == 's':
        if p2 == 'w':
            return False
        elif p2 == 'g':
            return True
    #Check For all Posibilities when computer choose w
    elif comp == 'w':
        if p2 == 'g':
            return False
        elif p2 == 's':
            return True
    #Check For all Posibilities when computer choose g
    elif comp == 'g':
        if p2 == 's':
            return False
        elif p2 == 'w':
            return True


print("Computer Turn: Snake(s) Water(w) and Gun(g)")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = "s"
elif randNo == 2:
    comp = "w"
elif randNo == 3:
    comp = "g"

p2 = input("Player's Turn: Snake(s) Water(w) and Gun(g)")

print("computer choose",comp)
print("you choose",p2)

a = gameWin(comp, p2)
if a == None:
    print("the game is tie")
elif a:
    print("You win the game")
else:
    print("you loose the game")










































