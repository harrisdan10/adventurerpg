#!/usr/bin/python3

from rooms import rooms
from player import player
from monster import monsters
from descriptions import descriptions
import time
from os import system, name
from actions import *

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


# def clear():
#     # for windows
#     if name == 'nt':
#         _ = system('cls')

#     # for mac and linux(here, os.name is 'posix')
#     else:
#         _ = system('clear')


def showStatus():
    global monster_type
    # clear()
    # print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    print()
    # print the current inventory
    print('Inventory : ' + str(inventory))
    print('Equipped : ', player_type["equipped_item"])
    print('Health: ', player_type["health"])
    if 'item' in rooms[currentRoom] and 'mini-boss' in rooms[currentRoom]['item'][0]:
        monster_type = monsters['Mini-Boss']
        print('Monster Health: ', monster_type['health'])
    elif 'item' in rooms[currentRoom] and 'boss' in rooms[currentRoom]['item'][0]:
        monster_type = monsters['Boss']
        print('Monster Health: ', monster_type['health'])
    else:
        print()
        print(rooms[currentRoom]['description'])
    print()
    if "item" in rooms[currentRoom]:
        delay(f"You see a {rooms[currentRoom]['item']}")
    print("---------------------------")


player_type = ''
monster_type = ''

def choose_player():
    global player_type
    player_info = ''
    while player_info == '' or player_info not in ["a", "aggressive", "d", "defensive"]:
        player_info = input("What is your game play style? ([A]ggressive or [D]efensive): ").lower()
        print(player_info)
        if player_info == "a" or player == "aggressive":
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

    if len(move) == 1:
        specify(move, inventory)

    elif move[0] == 'go':
        currentRoom = movement(move, rooms[currentRoom], currentRoom, player_type, monster_type)

    # if they type 'get' first
    elif move[0] == 'get':
        get_item(move, rooms[currentRoom], inventory, descriptions)

    elif move[0] == 'drop':
        drop_item(move, rooms[currentRoom], inventory)

    elif move[0] == 'inspect':
        inspect_item(move, currentRoom, descriptions)

    elif move[0] == 'equip' or move[0] == 'unequip':
        equip_item(move, inventory, player_type)

    elif move[0] == 'teleport' and 'magic stone' in inventory:
        currentRoom = teleport(move, rooms)

    if move[0] == 'extinguish' and currentRoom == 'West Hall':
        extinguish(move, rooms[currentRoom], descriptions)

    elif move[0] == 'pull':
        pull_handle(move, rooms[currentRoom])

    elif move[0] == 'q' or move[0] == 'quit':
        quit_game()

    if 'item' in rooms[currentRoom] and 'boss' in rooms[currentRoom]['item'][0] and player_type['equipped_item'] == "old cloak":
        boss_encounter(player_type, monster_type, rooms[currentRoom])

    if move[0] == 'fight':
        fight(player_type, monster_type, rooms[currentRoom])
