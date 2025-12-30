import pandas
#TODO 1. Create a dictionary in this format:
NATO = pandas.read_csv("nato_phonetic_alphabet.csv")
NATO_2 = NATO.to_dict()
NATO_dict = {value.letter:value.code for key, value in NATO.iterrows()}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
print(NATO_dict)

word = input("Input a word\n")
word_list = list(word)

print([NATO_dict[x.upper()] for x in word_list])
