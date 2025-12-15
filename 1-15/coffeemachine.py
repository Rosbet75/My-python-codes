#TODO 1. capture user input to know what to do next
#TODO 2. it must capture every time action is completed and cycle to serve to the next customer
#TODO 3. "off" must turn off the machine (finish execution of code)
#TODO 4. "report" must give reports of the current resources values
#TODO 5. check if enough resources to serve
#TODO 6. should prompt the user to insert coins and procecess them appropiately calculating the total value
#TODO 7. check if transaciton is succesful cheking the amount of money inserted is corredt after choosing the drink you are going to use
#TODO 8. if transcation is succesful the cost should be added as profit to the machine if too much money the machine should offer change
#TODO 9.
import sys
MENU = {
    "espresso":{
        "cost":1.5,
        "water":50,
        "coffee":18,
        "milk":0
    },
    "latte":{
        "cost":2.5,
        "water":200,
        "milk":150,
        "coffee":24
    },
    "capuccino":{
        "cost":3.0,
        "water":250,
        "milk":100,
        "coffee":24
    }
}

resources = {
    "water":2000,
    "coffee":2000,
    "milk":10000,
    "money":5000,
}
def report():
    print(f"Resource Values:\nWater:{resources['water']}\nMilk:{resources['milk']}\nCoffee:{resources['coffee']}\nMoney:{resources['money']}\n")

def money():
    print("Please enter your money:")
    string_list = ["How many quarters? ",
                   "How many dimes? ",
                   "How many nickles? ",
                   "How many pennies? "]
    money_list = []
    for item in string_list:
        money_list.append(int(input(item).strip()))
    return money_list[0] * 0.25 + money_list[1] * 0.10 + money_list[2] * 0.05 + money_list[3] * 0.01

def enough_resources(beverage):
    if resources["water"] >= beverage["water"] and resources["coffee"] >= beverage["coffee"] and resources["milk"] >= beverage["milk"]:
        return True
    else:
        return False
accion = ""
while accion != "exit":
    accion = input("What would you like?\n").strip().lower()

    if accion == "report":
        report()
    elif accion == "off":
        sys.exit()
    elif accion == "espresso" or accion == "latte" or accion == "capuccino":
        money_taken = money()
        change = 0
        print("You entered: $" + str(money_taken))
        while money_taken < MENU[accion]["cost"]:
            print(f"Not enough money, you need ${MENU[accion]["cost"] - money_taken} more")
            money_taken += money()
        if money_taken > MENU[accion]["cost"]:
            change = money_taken - MENU[accion]["cost"]
        if enough_resources(MENU[accion]):
            for key in resources:
                if key == "money":
                    resources[key] += money_taken
                else:
                    resources[key] -= MENU[accion][key]
            print("Here you go take your coffee!")
            if change > 0:
                print("Your change is $" + str(change))
    else:
        print("Input not recognized, try again")





