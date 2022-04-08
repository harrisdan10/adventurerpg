rooms = {
            'Basement' : {
                'up': 'Parlor',
                'north': 'Parlor',
                'item': ['note', 'oil', 'torch'],
                'description': "This room has an irregular flagstone tile floor. Crude chalk drawings adorn the floor. They appear to be pictures of beasts battling humans, and winning. Directly ahead you see a staircase leading upwards. The wall to your right is covered in green moss. It is thick and damp and appears that water seeps from the stone behind it. This room is unnaturally cold, a thin frost covers the walls and floor.The air in the room is clear and windy. The room smells stale. A loud banging noise can be heard."
            },
            'Parlor': {
                'down': 'Basement',
                'north': 'Kitchen',
                'south': 'Basement',
                'east': 'East Hall',
                'west': 'West Hall',
                'description': 'The first thing you notice upon enter the large room is  an oversized human-like handprint, about ten inches across, it is burned into the north wall leading into the Kitchen. You look around, taking in the room, noticing the has a limestone tile floor. The ceiling is a cathedral vaulted (multi-domed) and with the tattered remains of what once must have been colorful streamers hanging down to about eight feet from the floor. The walls of this room display a vivid scene as if one was centered in a forest meadow. The grass and trees sway as if blown by wind. Investigation reveals that this is due to a permanent illusion. Laying along the north wall is a partially intact human skeleton. To the east lays a dark hallway, the west another with a blazing fireplace. The air in the room is clear and drafty. The room smells putrid. A loud banging noise can be heard.'
            },
            'East Hall': {
                'west': 'Parlor',
                'east': 'Trap Room',
                'description': 'This hall has a smoothly hewn natural stone floor that have been polished smooth. A longs streak of blood or perhaps dark paint runs along what appears to be the length of the wall. The ceiling is a flat reinforced with stone beam with regular rectangular shaped beams as you process further down the hall small blue-green flames appear above-head seeming to guide you forward. A ratty old cloak hangs from a hook on one wall. The air in the hall feels heavy. The banging has ceased, but a loud slamming noise can be heard.'
            },
            'West Hall': {
                'east': 'Parlor',
                'down': 'Dungeon',
                'description': 'This hall has a smoothly hewn natural stone floor that have been polished smooth. All you can hear is the sound of the crackling fireplace and the banging as it grows louder with each step....You arrive at the end of the hall.',
                'item': 'Boss'
            },
            'Kitchen': {
                  'south': 'Parlor',
                  'west': 'Dining Room',
                  'description': ''
                },
            'Dining Room': {
                  'east': 'Kitchen',
                  'description': '"A large rounded stone table sits at the center of the room. A singular plate rest on it, the food spoiled and surrounded by flies. The ceiling is a flat with wooden planks reinforced with regular wooden beams and appears broken and cracked. Near the east wall a human skull has been mounted on a broken spear shaft that has been stuck in the floor.The air in the room is foggy. The room smells of Rotting vegetation. A faint banging noise can be heard. Nothing else of note is in this room."'
               },
}