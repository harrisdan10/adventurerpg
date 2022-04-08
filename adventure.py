#!/usr/bin/python3

from rooms import rooms
import sys

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
    # print a main menu and the commands
    print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')


def showStatus():
    # print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print the current inventory
    print('Inventory : ' + str(inventory))
    # print an item if there is one
    if "item" in rooms[currentRoom]:
        print(f"You see a {rooms[currentRoom]['item']}")
    print("---------------------------")


# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms


# start the player in the Hall
currentRoom = 'Basement'

showInstructions()

# loop forever
while True:

    showStatus()

    # get the player's next 'move'
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]
    move = move.lower().split(" ", 1)

    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    # if they type 'get' first
    if move[0] == 'get':
        # if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            inventory.append(move[1])
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item from the room
            del rooms[currentRoom]['item']
        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    if move[0] == 'equip':
        if move[1] in inventory:
            print(f"{move[1]} equipped!")
        else:
            print(f"You don't have a {move[1]} in your inventory!")

    if move[0] == 'q' or move[0] =='quit':
        quitResponse = input('Are you you sure you want to quit? (Y|N): ').strip().lower()
        if quitResponse == 'y' or quitResponse == 'yes':
            print('Thank you for playing! Quitters never prosper!')
            sys.exit()
        else:
            pass

    ## Define how a player can win
    if currentRoom == 'Boss Location' and 'sword' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break
    elif currentRoom == 'Boss Location' and 'sword' not in inventory:
        print('The Boss ....... GAME OVER!')
        break
    ## If a player enters a room with mini boss
    elif currentRoom == 'East Hall' and '' in inventory:
        print('')
        break
    elif currentRoom == 'East Hall' and '' not in inventory:
        print('')
        break