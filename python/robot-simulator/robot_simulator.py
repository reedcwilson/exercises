

NORTH = (0, 1)
EAST = (1, 0)
SOUTH = (0, -1)
WEST = (-1, 0)


class Robot(object):

    def __init__(s, bearing=NORTH, x=0, y=0):
        s.bearing = bearing
        s.coordinates = (x, y)
        s.commands = {'A': s.advance, 'R': s.turn_right, 'L': s.turn_left}

    def advance(s):
        x, y = s.bearing
        s.coordinates = (s.coordinates[0] + x, s.coordinates[1] + y)

    def turn_right(s):
        s.bearing = (s.bearing[1], -s.bearing[0])

    def turn_left(s):
        s.bearing = (-s.bearing[1], s.bearing[0])

    def simulate(s, command_str):
        for command in command_str.upper():
            s.commands[command]()
