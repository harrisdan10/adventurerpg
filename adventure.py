#!/usr/bin/python3

from rooms import rooms
from player import player
import sys
import string
import time
from os import system, name
from playsound import playsound
import requests
import random

URL = 'https://cat-fact.herokuapp.com/facts'
# playsound('adventure.mp3', False)

# Replace RPG starter project with this code when new instructions are live
# def cat_facts():
#     cat = requests.get(URL).json()
#     catFacts = []
#     for meow in cat:
#         catFacts.append(meow.get("text"))
#     print(random.choice(catFacts))


def delay(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(.03)
    print()

def showInstructions():
    # print a main menu and the commands
    print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def showStatus():
    # clear()
    # print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    print()
    # print the current inventory
    print('Inventory : ' + str(inventory))
    print('Health: ', player_type["health"])
    print()
    print(rooms[currentRoom]['description'])
    print()

    # print an item if there is one
    if "item" in rooms[currentRoom]:
        for item in rooms[currentRoom]['item']:
            delay(f"You see a {list(item.keys())}")
    print("---------------------------")


player_type = ''


def choose_player():
    global player_type
    player_info = ''
    while player_info == '':
        player_info = input("What is your game play style? ([A]ggressive or [D]efensive): ").lower()

        if player_info == "A" or player == "aggressive":
            player_type = player["Attack"]
        else:
            player_type = player["Defensive"]


choose_player()
# an inventory, which is initially empty
inventory = player_type['inventory']

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
        for item in rooms[currentRoom]['item']:
            # if the room contains an item, and the item is the one they want to get
            if "item" in rooms[currentRoom] and move[1] in list(item.keys()):
                # add the item to their inventory
                inventory.append(move[1])

                # display a helpful message
                print(f"{move[1]} got!")
                if "description" in item[move[1]]:
                    print(f"{rooms[currentRoom]['item'][0][move[1]]['description']}")
                else:
                    print(f"{item[move[1]]}")
                # delete the item from the room
                item_index = list(item.keys()).index(move[1])
                if list(item.keys())[item_index] == move[1]:
                    # print('deleted')
                    del rooms[currentRoom]['item'][0][move[1]]
                    if len(rooms[currentRoom]['item'][0]) == 0:
                        del rooms[currentRoom]['item']

            # otherwise, if the item isn't there to get
            else:
                # tell them they can't get it
                print(f"Can\'t get {move[1]} !")

    if move[0] == 'approach':
        cat = requests.get(URL).json()
        catFacts = []
        for meow in cat:
            catFacts.append(meow.get("text"))
        if move[1] in '' and currentRoom == '':
            print(f"All-knowing Sphinx: {random.choice(catFacts)}")
        else:
            print(f"The All-knowing Sphinx is not in this room!")

    if move[0] == 'equip':
        if move[1] in inventory:
            print(f"{move[1]} equipped!")
        else:
            print(f"You don't have a {move[1]} in your inventory!")

    if move[0] == 'teleport' and 'magic stone' in inventory:
        room = string.capwords(move[1].title())
        if room in list(rooms.keys()):
            currentRoom = room
            print(f"You are now in the {room}!")
        else:
            print(f"You don't have a magic stone in your inventory!")

    if move[0] == 'drop':
        # check that they are allowed wherever they want to go
        if move[1] in inventory:
            # set the current room to the new room
            if 'item' not in rooms[currentRoom]:
                rooms[currentRoom]['item'] = [move[1]]
                inventory.remove(move[1])
                print(f'{move[1]} was dropped')
            else:
                rooms[currentRoom]['item'][0][move[1]] = (move[1])
                inventory.remove(move[1])
                print(f'{move[1]} was dropped')
        # there is no door (link) to the new room
        else:
            print("You currently have nothing to drop")

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
    # If a player enters a room with mini boss
    elif currentRoom == 'East Hall' and '' in inventory:
        print('')
        break
    elif currentRoom == 'East Hall' and '' not in inventory:
        print('')
        break