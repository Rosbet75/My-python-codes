import random


choice = int(input("What do you choose? Type 0 for rock, 1 for paper, or 2 for scissors\n"))
mapa = {0:"Rock", 1:"Paper", 2:"Scissors"}
print(f"You chose: {mapa[choice]}")
computer_choice = random.randint(0, 2)
print(f"Computer chose: {mapa[computer_choice]}")

concat = str(choice) + str(computer_choice)

if concat == "01" or concat == "12" or concat == "20":
    print("You lose")
elif concat == "02" or concat == "10" or concat == "21":
    print("You win")
elif choice == computer_choice:
    print("A draw")