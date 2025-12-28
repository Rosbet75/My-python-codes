#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

import copy
with open("./Input/Names/invited_names.txt", "r") as file, open("./Input/Letters/starting_letter.txt", "r") as file2:
    template = file2.readlines()
    for line in file:
        with open(f"./Output/ReadyToSend/{line.strip()}.txt", "w") as letter:
            final_letter = copy.deepcopy(template)
            final_letter[0] = final_letter[0].replace("[name]", line.strip())
            print(final_letter)
            for x in final_letter:
                letter.write(x)

