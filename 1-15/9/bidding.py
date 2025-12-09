import os
bidders = {}
more_bids = "yes"
while more_bids == "yes":
    name = input("What is your name? \n").strip()
    amount = int(input("How much would you like to bid? $").strip())
    bidders[name] = amount
    more_bids = input("Are there more bids yes/no").strip()
    while more_bids != "yes" and more_bids != "no":
        more_bids = input("Wrong input only yes or no option").strip()
    os.system('cls')
winner = ""
biggest = 0
for key, value in bidders.items():
    bigges = value if value > biggest else biggest
    winner = key

print(f"The winner of the bid {winner} with ${biggest} dollars\n")