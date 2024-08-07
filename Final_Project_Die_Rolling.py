#Die Rolling

import random

#Roll a [type] di(c)e [amount] numeber of times, returns a list of the rolls
def rollDice(type, amount):
    roll = []
    for i in range(amount):
       num = random.randint(1, type)
       roll.append(num)
    return roll

#Gathers what kind of di(c)e to roll, returns an int
def dieType():
    i = 0 
    while i != 1:
        print("What kind of die do you want rolled? (Type 'help' or 'info' in you are unsure)")
        userInput = input()
        if userInput.lower() == 'help' or userInput.lower() == 'info':
            print("Enter the number of the sides of the di(c)e you want.")
        elif userInput.isdigit() == True:
            dieType = int(userInput)
            i += 1
        else:
            print("Invalid entry.")
    return dieType

#Gathers how many di(c)e to roll, returns an int
def dieAmount():
    print("How many di(c)e do you want to roll?")
    userInput = input()
    if userInput.isdigit() == True:
        if userInput == 0:
            print("Then why are you here?")
        else:
            amount = int(userInput)
    return amount

#Actually rolls the di(c)e, calls the other functions
def rollTheDice():
    type = dieType()
    amount = dieAmount()

    roll = rollDice(type, amount)
    print(roll)

def rollInitiative():
    initiative = rollDice(20, 2)
    return initiative

def rollToHit():
    roll = rollDice(10, 2)
    hit = int(roll[0]) + int(roll[1])
    return hit

def rollDamage():
    roll = rollDice(6, 2)
    damage = int(roll[0] + roll[1])
    return damage
