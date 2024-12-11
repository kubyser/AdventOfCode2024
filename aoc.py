DIRECTIONS = {"N":(0,-1), "NE":(1,-1), "E":(1,0), "SE":(1,1), "S":(0,1), "SW":(-1,1), "W":(-1,0), "NW":(-1,-1)}

def stringsArrayToLists(lines, op = lambda x: x):
    width = len(lines[0])
    height = len(lines)
    data = [[None for x in range(width)] for y in range(height)]
    for y,l in enumerate(lines):
        for x,c in enumerate(l):
            data[y][x] = op(c)
    return data, height, width