rooms = {
            'Basement' : {
                'up': 'Parlor',
                'item': ['note', 'oil', 'torch'],
                'description': "The door is made of a fabric curtain, it has a wood bolt on the inside and is painted red, probably several years old. This room has an irregular flagstone tile floor. Crude chalk drawings adorn the floor. They appear to be pictures of goblins battling humanoids, and winning. The ceiling is a cathedral vaulted (multi-domed) and with the tattered remains of what once must have been colorful streamers hanging down to about eight feet from the floor. The wall to your right is covered in green moss. It is thick and damp and appears that water seeps from the stone behind it. This room is unnaturally cold, a thin frost covers the walls and floor.The air in the room is clear and windy. The room smells stale. A loud banging noise can be heard."
            },
            'Parlor': {
                'down': 'Basement',
                'north': 'Kitchen',
                'south': '',
                'east': 'East Hall',
                'west': 'West Hall',
                'description': ''
            },
            'Kitchen': {
                  'south': 'Parlor',
                  'west': 'Dining Room',
                  'item': 'monster',
                  'description' : ''
                },
            'Dining Room': {
                  'east': 'Kitchen',
                  'description': ''
               },
}