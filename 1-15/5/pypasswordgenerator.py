import random
from math import acosh

print("Welcome to the PyPassword Generator")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"how many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pass_array = []
sete = [nr_letters, nr_symbols, nr_numbers]
for i in range(0, len(sete)):
    for x in range(1, sete[i] + 1):
        num = 0
        if i == 0:
            if random.randint(0, 1):
                num = random.randint(65, 90)
            else:
                num = random.randint(97, 122)
        elif i == 1:

            num = random.randint(33, 47)
        elif i == 2:
            num = random.randint(48, 57)

        pass_array.append(num)
cadena = []
for i in pass_array:
    cadena.append(chr(i))
random.shuffle(cadena)

final = ""
for i in cadena:
    final += i

print(final)
# for i in range(1, (nr_numbers + nr_symbols + nr_letters) + 1):
#     random.