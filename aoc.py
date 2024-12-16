DIRECTION_MOVEMENT = {"N":(0, -1), "NE":(1, -1), "E":(1, 0), "SE":(1, 1), "S":(0, 1), "SW":(-1, 1), "W":(-1, 0), "NW":(-1, -1)}
DIRECTIONS_MAIN = ("N", "E", "S", "W")
TURNS = {"N": {"L": "W", "R": "E"}, "S": {"L": "E", "R": "W"}, "E": {"L": "N", "R": "S"}, "W": {"L": "S", "R": "N"}, }

def stringsArrayToLists(lines, op = lambda x: x):
    width = len(lines[0])
    height = len(lines)
    data = [[None for x in range(width)] for y in range(height)]
    for y,l in enumerate(lines):
        for x,c in enumerate(l):
            data[y][x] = op(c)
    return data, height, width


def addCoords(c1, c2):
    if len(c1) != len(c2):
        print(f"ERROR: addCorrds with different vector sizes: {c1}, {c2}")
        exit(-1)
    return tuple((x+y for (x,y) in zip(c1, c2)))
