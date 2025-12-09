tipo = input("Type 'encode' to encrypt, type 'decode' to decrypt\n")
while tipo != "encode" and tipo != "decode":
    tipo = input("Wrong input try again").strip().lower()
text = input("type your text").strip().lower()
number = int(input("type your number").strip())

def char_shifter(caracter, num):
    if caracter + num > 24:
        caracter = caracter + num - 26
    else:
        caracter = caracter + num
    return caracter
def char_shifter_reverse(caracter, num):
    if caracter - num < 0:
        caracter = caracter - num + 26
    else:
        caracter = caracter - num
    return caracter

# character = 0
# print(f"caracter de prueba: {chr(character + 97)}")
# print(chr(char_shifter_reverse(character, number)+97))
# if type == "encode":
if tipo == "encode":
    transformed = [chr(char_shifter(ord(x) - 97, number) + 97) for x in text]
else:
    transformed = [chr(char_shifter_reverse(ord(x) - 97, number) + 97) for x in text]
# elif type == "decode":
#transformed = [chr(char_shifter(ord(x) - 97, number) + 97) for x in text]
print(''.join(transformed))