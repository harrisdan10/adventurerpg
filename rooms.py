from descriptions import descriptions

rooms = {
            'Basement': {
                'up': 'Parlor',
                'north': 'Parlor',
                'item': [{
                    'note': {
                        'description': 'placeholder note'
                    },
                    'oil': {
                        'description': 'A smooth, thick liquid that is used as a fuel or can be used to coat an item and set it ablaze.'
                    },
                    'torch': {
                        'description': 'A handheld burning fire that burns bright and serves to be a guide in the darkness.'

                    }
                        }],
                'description': "The room has an irregular flagstone tile floor. Crude chalk drawings adorn the floor\n"
                               "There's a portrait of beasts battling humans, and winning. Directly ahead you see a\n"
                               "staircase leading upwards. he wall to your right is covered in green moss. It is\n"
                               "thick and damp and appears that water seeps from the stone behind it.This room\n"
                               "is unnaturally cold, a thin frost covers the walls and floor. The air in the room\n"
                               "is clear and windy. The room smells stale. A loud banging noise can be heard."
            },
            'Parlor': {
                'down': 'Basement',
                'north': 'Kitchen',
                'south': 'Basement',
                'east': 'East Hall',
                'west': 'West Hall',
                'item': [{'sword': {
                    'description': 'A weapon with a long, straight, sharp-edged blade that can be used to slay an enemy.'
                    }}],
                'description': 'The first thing you notice upon enter the large room is  an oversized human-like handprint, about ten inches across,\nit is burned into the north wall leading into the Kitchen. You look around, taking in the room, noticing the has a limestone tile floor.\nThe ceiling is a cathedral vaulted (multi-domed) and with the tattered remains of what once must have been colorful streamers hanging down\nto about eight feet from the floor. The walls of this room display a vivid scene as if one was centered in a forest meadow.\nThe grass and trees sway as if blown by wind. Investigation reveals that this is due to a permanent illusion. Laying along the north wall\nis a partially intact human skeleton. To the east lays a dark hallway, the west another with a blazing fireplace.\nThe air in the room is clear and drafty. The room smells putrid. A loud banging noise can be heard.'
            },
            'East Hall': {
                'west': 'Parlor',
                'east': 'Trap Room',
                'item': [{'old cloak':{
                    'description': 'A cloak made of a special type of material that is designed to conceal its wearer.'
                        }}],
                'description': 'This hall has a smoothly hewn natural stone floor that have been polished smooth. A longs streak of blood or perhaps dark\npaint runs along what appears to be the length of the wall. The ceiling is a flat reinforced with stone beam with regular rectangular shaped beams as you process\nfurther down the hall small blue-green flames appear above-head seeming to guide you forward. A ratty old cloak hangs from a hook on one wall.\nThe air in the hall feels heavy. The banging has ceased, but a loud slamming noise can be heard.'
            },
            'West Hall': {
                'east': 'Parlor',
                'item': [{'fireplace': {
                    'description': 'Behind the blazing flames you see a handle.',
                    'description_2': 'You see a handle at the back of the fireplace',
                    'blazing': True
                        }}],
                'description': 'This hall has a smoothly hewn natural stone floor that have been polished smooth. All that can be heard is the sound of the crackling\nfireplace and a loud banging which seems to grows louder with each step....You arrive at the end of the hall.\n'
            },
            'Kitchen': {
                  'south': 'Parlor',
                  'west': 'Dining Room',
                  'description': ''
                },
            'Dining Room': {
                  'east': 'Kitchen',
                  'north': 'Secret Door',
                  'description': '"A large rounded stone table sits at the center of the room. A singular plate rest on it, the food spoiled and surrounded by flies. The ceiling is a flat with wooden planks reinforced with regular wooden beams and appears broken and cracked. Near the east wall a human skull has been mounted on a broken spear shaft that has been stuck in the floor.The air in the room is foggy. The room smells of Rotting vegetation. A faint banging noise can be heard. Nothing else of note is in this room."'
            },
            'Trap Room': {
                'west': 'East Hall',
                'item': [{'mini-boss': {
                    'description': 'mini-boss'
                }}],
                'description': 'The beasts body lays before you sprawled out on the floor. The stench of blood and urine fills the air'
                },
            'Secret Door': {
                'south': 'Kitchen',
                'item': [{'magic stone': {
                    'description': 'The magic stone has the ability of teleporting you to any room in an instant.'
                }}],
                'description': 'Congratulations! You have opened the secret door which holds something very powerful inside.'
            },
            'Boss Room': {
                'item': [{'boss': {
                    'description': 'boss'
                }}],
                'description': ''
            }
}