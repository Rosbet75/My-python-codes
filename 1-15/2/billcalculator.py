print("Welcome to the tip calculator!")
total = float(input("What was the total bill?\n$"))
tip_amount = int(input("How much tip would you like to give? 10, 12 or 13\n"))
people = int(input("How many people to split the bill?\n"))
result = (total + ((tip_amount / 100 * total)))/people
print(f"Each person should pay ${result}")