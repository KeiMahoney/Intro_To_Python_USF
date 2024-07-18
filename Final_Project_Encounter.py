#Make sure to mention in the blog post that the stats were modified from D&D Beyond. 
#Mainly that they were vastly simplified, this is just a very bare bones simulation, made to 
#give an idea of what encounters are kind of like.
#D&D Encounter Simulation (Simplified)

import random
import Final_Project_Die_Rolling

creatureList = open("Final_Project_Creatures.txt").read().split("\n")
characterList = open("Final_Project_Characters.txt").read().split("\n")

#Creates a monster from the creatureList global variable
def makeMonster():
    monster = []
    chosenMonster = creatureList[random.randint(0,9)].split(';')
    for item in chosenMonster:
        monster.append(item)
    return monster

#Creates a character from the characterList global variable
def makeCharacter():
    character = []
    chosenCharacter = characterList[random.randint(0,4)].split(';')
    for item in chosenCharacter:
        character.append(item)
    return character

#Displays the health of a [character] and [monster] at the given moment
def displayHealth(character, monster, cHealth, mHealth):
    print(character[0] + ": " + str(cHealth))
    print(monster[0] + ": " + str(mHealth))

#Creates a mock fight with a [character] and [monster] 
def encounter(character, monster):
    monsterHealth = int(monster[1])
    characterHealth = int(character[1])
    
    print(monster[4])
    print(character[3])
    print()

    print("Health")
    displayHealth(character, monster, characterHealth, monsterHealth)
    print()

    print("Roll Initiative!")
    initiative = Final_Project_Die_Rolling.rollInitiative()
    character.append(initiative[0])
    print(character[0] + ": " + str(character[4]))
    monster.append(initiative[1])
    print(monster[0] + ": " + str(monster[5]))


    if character[4] >= monster[5]: #Using the "meets it, beats it" rule
        print("You gain the upper hand! You attack first.")
        print()
        while monsterHealth > 0 and characterHealth > 0:
            characterHit = Final_Project_Die_Rolling.rollToHit()
            if characterHit >= int(monster[3]) and characterHealth > 0:
                characterAttack = Final_Project_Die_Rolling.rollDamage()
                monsterHealth -= characterAttack
                print("Your blow lands, dealing " + str(characterAttack) + " damage!")
                displayHealth(character, monster, characterHealth, monsterHealth)
                print()
            else:
                print("Your attack misses your opponent.")
                displayHealth(character, monster, characterHealth, monsterHealth)
                print()

            monsterHit = Final_Project_Die_Rolling.rollToHit()
            if monsterHit >= int(character[2]) and monsterHealth > 0:
                monsterAttack = int(monster[2])
                characterHealth -= monsterAttack
                print("The " + monster[0] + "'s blow lands, dealing " + str(monsterAttack) + " damage!")
                displayHealth(character, monster, characterHealth, monsterHealth)
                print()
            else:
                print("The " + monster[0] + " misses their attack.")
                displayHealth(character, monster, characterHealth, monsterHealth)
                print()
        
        if characterHealth > 0:
            print()
            displayHealth(character, monster, characterHealth, monsterHealth)
            print("You killed the " + monster[0] + "! Good job!")
        elif monsterHealth > 0:
            print()
            displayHealth(character, monster, characterHealth, monsterHealth)
            print("You were killed by the " + monster[0] + ". Maybe another adventurer will defeat it...")
    else:
        print("The monster got the upper hand! It attacks first.")
        print()
        while monsterHealth > 0 and characterHealth > 0:
            monsterHit = Final_Project_Die_Rolling.rollToHit()
            if monsterHit >= int(character[2]) and monsterHealth > 0:
                monsterAttack = int(monster[2])
                characterHealth -= monsterAttack
                print("The " + monster[0] + "'s blow lands, dealing " + str(monsterAttack) + " damage!")
                displayHealth(character, monster, characterHealth, monsterHealth)
                print()
            else:
                print("The " + monster[0] + " misses their attack.")
                displayHealth(character, monster, characterHealth, monsterHealth)
                print()
                

            characterHit = Final_Project_Die_Rolling.rollToHit()
            if characterHit >= int(monster[3]) and characterHealth > 0:
                characterAttack = Final_Project_Die_Rolling.rollDamage()
                monsterHealth -= characterAttack
                print("Your blow lands, dealing " + str(characterAttack) + " damage!")
                displayHealth(character, monster, characterHealth, monsterHealth)
                print()
            else:
                print("Your attack misses your opponent.")
                displayHealth(character, monster, characterHealth, monsterHealth)
                print()
        
        if characterHealth > 0:
            print()
            displayHealth(character, monster, characterHealth, monsterHealth)
            print("You killed the " + monster[0] + "! Good job!")
        elif monsterHealth > 0:
            print()
            displayHealth(character, monster, characterHealth, monsterHealth)
            print("You were killed by the " + monster[0] + ". Maybe another adventurer will defeat it...")

#Runs an instance of the encounter function
encounter(makeCharacter(), makeMonster())