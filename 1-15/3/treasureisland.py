def choice(cad, comp1, comp2):
    x = input(cad + "\n")
    if x == comp1 or x == comp2:
        return x
    else:
        while (cad != comp1 or x != comp2):
            x = input("Wrong input, try again:\n")
        return x


def gameover():
    print("Game over, loser")
    exit()



print("Welcome to Treasure Island\nYour mission is to find the treasure.")
direction1 = choice("left or right", "left", "right")
if direction1 == "right":
    gameover()

direction2 = choice("Swim or wait", "swim", "wait")

if direction2 == "swim":
    gameover()

direction3 = input("red or blue? or yellow?")
if direction3 == "blue" or direction3 == "yellow":
    gameover()



