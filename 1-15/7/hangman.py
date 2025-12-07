import random
word_list = [
    "nebula",
    "travesía",
    "cobalto",
    "madrugada",
    "umbral",
    "quimera",
    "silente",
    "bruma",
    "vértigo",
    "cántaro",
    "cenit",
    "marea",
    "destello",
    "crisol",
    "arcano"
]

tries = 6

print("Welcome to hangman try to guess the word")
def letter_catcher():
    choice = input("Guess the next letter").lower()
    while not (len(choice) == 1 and 97 <= ord(choice[0]) <= 122):
        choice = input("Wrong input try again").lower()
    return choice
chosen_word = word_list[random.randint(1, len(word_list))]
veil_word = ["_" for i in chosen_word]
while tries != 0 :
    if "_" not in veil_word:
        print("You pretty cool ngl, you won!")
        exit(0)
    choice = letter_catcher()
    if choice in chosen_word:
        print("Correct!!")
        for i in range(0, len(chosen_word)):
            if choice == chosen_word[i]:
                veil_word[i] = choice
    else:
        print("You suck, you lose one life")

        tries -= 1
        print(f"Remaining lifes: {tries}")

    print(*veil_word)


if tries == 0:
    print("You lost, you suck")
