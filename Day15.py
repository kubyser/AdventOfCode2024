DIRECTIONS = {"^":(0,-1), ">":(1,0), "v":(0,1), "<":(-1,0)}

def getMove(pos, direction):
    return pos[0]+DIRECTIONS[direction][0], pos[1]+DIRECTIONS[direction][1]

def getNextEmpty(pos, direction):
    x, y = pos
    while True:
        x, y = getMove((x,y), direction)
        if data[y][x] == '.':
            return x,y
        if data[y][x] == '#':
            return None

def printMap():
    for l in data:
        s = ""
        for c in l:
            s += c
        print(s)

lines = [l.removesuffix("\n") for l in open("resources/day15_input.txt", "r")]
width = len(lines[0])
height = 0
data = []
robot = (None, None)
l = lines.pop(0)
while l != "":
    data.append([])
    for x, c in enumerate(l):
        if c == '@':
            robot = (x, height)
            data[height].append('.')
        else:
            data[height].append(c)
    height += 1
    l = lines.pop(0)
moves = ""
while len(lines) > 0:
    l = lines.pop(0)
    moves += l
#print(data)
#print(moves)
for move in moves:
    np = getNextEmpty(robot, move)
    if np is None:
        continue
    robot = getMove(robot, move)
    if robot != np:
        data[np[1]][np[0]] = 'O'
        data[robot[1]][robot[0]] = '.'
printMap()
sumCoords = sum([x+y*100 for y,l in enumerate(data) for x,c in enumerate(l) if data[y][x] == 'O'])
print(f"Sum of boxes coordinates: {sumCoords}")








