import sys
import random
import string
import requests


# function to handle player movement
def movement(move, location, current_room, player, monster):
    if move[1] in location:
        # check if location has 'item' property. If so is 'mini-boss' a value
        if 'item' in location and 'mini-boss' in location['item'][0]:
            print('There is no escape. It is kill or be killed! You must fight!')
            return current_room
        else:
            # set the current room to the new room
            room = location[move[1]]
            return room
    # there is no door (link) to the new room
    else:
        print('You can\'t go that way!')
        return current_room


# function that allows player to teleport to any room
def teleport(move, rooms):
    room = string.capwords(move[1].title())
    if room in list(rooms.keys()):
        current_room = room
        print(f"You are now in the {room}!")
        return current_room
    else:
        print(f"You don't have a magic stone in your inventory!")


# function to inspect items
def inspect_item(move, current_room, location):
    # check if item (move[1]) is in current room
    if move[1] in location['item'][0]:
        if move[1] == 'sphinx' and current_room == 'Kitchen':
            url = 'https://cat-fact.herokuapp.com/facts'
            cat = requests.get(url).json()
            cat_facts = []
            for meow in cat:
                cat_facts.append(meow.get("text"))
            print(f"All-knowing Sphinx: {random.choice(cat_facts)}")
    # check if the blazing property of West Hall fireplace is false
    if not location['item'][0]['fireplace']['blazing']:
        print(location['item'][0][move[1]]["description_2"])
    else:
        print(location['item'][0][move[1]]["description"])


def get_item(move, location, inventory):
    for item in location['item']:
        # if the room contains an item, and the item is the one they want to get
        if "item" in location and move[1] in list(item.keys()):
            if move[1] in ["mini-boss", "boss", "fireplace"]:
                print('Come on now...')
            # add the item to their inventory
            else:
                inventory.append(move[1])

                # display a helpful message
                print(f"{move[1]} got!")
                # check if the item has a description property
                if "description" in item[move[1]]:
                    print(f"{location['item'][0][move[1]]['description']}")
                else:
                    print(f"{item[move[1]]}")
                # delete the item from the room
                item_index = list(item.keys()).index(move[1])
                if list(item.keys())[item_index] == move[1]:
                    # print('deleted')
                    del location['item'][0][move[1]]
                    if len(location['item'][0]) == 0:
                        del location['item']

            # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print(f"Can\'t get {move[1]} !")


def drop_item(move, location, inventory):
    if move[1] in inventory:
        # set the current room to the new room
        if 'item' not in location:
            location['item'] = [move[1]]
            inventory.remove(move[1])
            print(f'{move[1]} was dropped')
        else:
            location['item'][0][move[1]] = (move[1])
            inventory.remove(move[1])
            print(f'{move[1]} was dropped')
    # there is no door (link) to the new room
    else:
        print("You currently have nothing to drop")


def equip_item(move, inventory, player):
    if move[0] == "equip":
        if move[1] in inventory:
            print(f"{move[1]} equipped!")
            player['equipped_item'] = move[1]
            print(player['equipped_item'])
        else:
            print(f"You don't have a {move[1]} in your inventory!")
    else:
        if move[1] in inventory:
            print(f"{move[1]} unequipped!")
            player['equipped_item'] = ''
            print(player['equipped_item'])
        else:
            print(f"You don't have a {move[1]} in your equipped!")


def extinguish(move, location):
    if move[1] == "fire" or move[1] == "fireplace":
        print('The fire has been put out')
        # change West Hall fireplace blazing property to false
        location['item'][0]['fireplace']['blazing'] = False
    elif move[1] == "fire" or move[1] == "fireplace" and location['item'][0]['fireplace']['blazing'] == False:
        print("Fireplace already extinguished.")
    else:
        print("There is nothing to extinguish.")


def pull_handle(move, location):
    if move[1] == "handle":
        print('You pull the handle and the north wall crumbles, revealing a staircase leading down')
        location['down'] = 'Boss Room'
    else:
        print("There is nothing to pull")


def quit_game():
    quit_response = input('Are you you sure you want to quit? (Y|N): ').strip().lower()
    if quit_response == 'y' or quit_response == 'yes':
        print('Thank you for playing! Quitters never prosper!')
        sys.exit()
    else:
        pass


# variable used to track how close player is to special availability
special_gauge = 0
# countdown variable to monster strike
monster_strike_counter = 2


def fight(player, monster, location):
    global special_gauge
    global monster_strike_counter

    if monster_strike_counter != 0:
        special_gauge += 1
        monster_strike_counter -= 1
        if special_gauge == 3:
            special = ''
            while special == '' or special not in ['y', 'n', 'yes', 'no']:
                special = input("With every strike you felt you energy swell. It has now reach its limit.\n"
                                "Your special is available. Would you like to use it?\n").lower()
                # check value of special
                if special == 'n' or special == 'no':
                    if player['equipped_item'] == 'sword':
                        player_dmg = random.choice(player['attack']) * 2
                    else:
                        player_dmg = random.choice(player['attack'])
                else:
                    if player['equipped_item'] == 'sword':
                        player_dmg = player['special'] * 2
                    else:
                        player_dmg = player['special']
                print(f'You strike the beast dealing {player_dmg} damage')
                monster['health'] -= player_dmg
                special_gauge = 0
        else:
            if player['equipped_item'] == 'sword':
                player_dmg = random.choice(player['attack']) * 2
            else:
                player_dmg = random.choice(player['attack'])
            print(f'You strike the beast dealing {player_dmg} damage')
            monster['health'] -= player_dmg
    # if monster strike counter is 0 monster will attack and counter is reset
    else:
        monster_dmg = random.choice(monster['attack'])
        if monster_dmg == 0:
            print('You managed to evade the beasts strike.')
            monster_strike_counter = 2
        else:
            print(f'The beast strikes dealing {monster_dmg} damage')
            monster_strike_counter = 2
            player['health'] -= monster_dmg

    if monster['health'] <= 0:
        # check if mini-boss is in current room, if so delete
        if 'mini-boss' in location['item'][0]:
            del location['item'][0]['mini-boss']
            # if not mini-boss only other monster option is boss which will be deleted
        else:
            del location['item'][0]['boss']
            print('You managed to defeat the beast, revealing a door on the far side of the room.\n'
                'You open it and are teleported outside. You appear to have escaped! You win!')
            sys.exit()

    if player['health'] <= 0:
        print('You were defeated by the beast. Sadly, your journey has ended.')
        sys.exit()


# variable to control whether player chooses to fight boss
fighter = False


def boss_encounter(player, monster, location):
    global fighter
    fight_flight = ''
    if not fighter:
        while fight_flight == '' or fight_flight not in ['y', 'n', 'yes', 'no']:
            fight_flight = input('For some reason the beast has not detected you. Do you want to fight?\n'
                                 '[Y/N]\n').lower()
            if fight_flight == 'y' or fight_flight == 'yes':
                fighter = True
                fight(player, monster, location)
            else:
                print('You sneak past the beast to a door on the far side of the room.\n'
                      'You open it and are teleported outside.\n'
                      'You appear to have escaped. You win!')
                sys.exit()


def specify(move, inventory):
    if move[0] in ['get', 'drop', 'inspect', 'equip', 'unequip']:
        print(f'{move[0]} what?')
    elif move[0] == 'go':
        print(f'{move[0]} where?')
    elif move[0] == 'teleport' and 'magic stone' not in inventory:
        print(f'You need magic stone to {move[0]}')

