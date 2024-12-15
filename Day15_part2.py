DIRECTIONS = {"^":(0,-1), ">":(1,0), "v":(0,1), "<":(-1,0)}

def getMove(pos, direction):
    return pos[0]+DIRECTIONS[direction][0], pos[1]+DIRECTIONS[direction][1]


def getBoxCanMove(boxId, direction):
    posToCheck = set()
    if direction == '<':
        posToCheck.add(getMove(boxes[boxId][0], direction))
    elif direction == '>':
        posToCheck.add(getMove(boxes[boxId][1], direction))
    elif direction in ('^', 'v'):
        posToCheck.add(getMove(boxes[boxId][0], direction))
        posToCheck.add(getMove(boxes[boxId][1], direction))
    touchesBoxes = set()
    for (x,y) in posToCheck:
        if (x,y) in walls:
            return False, None
        if (x,y) in boxMap:
            touchesBoxes.add(boxMap[(x,y)])
    chainedBoxes = {boxId}
    if len(touchesBoxes) == 0:
        return True, chainedBoxes
    for nextBox in touchesBoxes:
        canMove, depBoxes = getBoxCanMove(nextBox, direction)
        if not canMove:
            return False, None
        chainedBoxes = chainedBoxes.union(depBoxes)
    return True, chainedBoxes

def moveBox(box, direction):
    for c in (0,1):
        if boxMap[boxes[box][c]] == box:
            boxMap.pop(boxes[box][c])
    newPos = [getMove(boxes[box][boxPart], direction) for boxPart in (0,1)]
    boxes[box] = newPos
    boxMap[newPos[0]] = box
    boxMap[newPos[1]] = box


def printMap():
    for y in range(height):
        s = ''
        x = 0
        while x < width:
            if (x,y) in walls:
                s += '#'
            elif (x,y) in boxMap:
                s += '[]'
                x += 1
            elif (x,y) == robot:
                s += '@'
            else:
                s += '.'
            x += 1
        print(s)

lines = [l.removesuffix("\n") for l in open("resources/day15_input.txt", "r")]
robot = (None, None)
walls = set()
boxes = {}
boxMap = {}
boxNum = 0
l = lines.pop(0)
width = len(l)*2
y = 0
while l != "":
    for x, c in enumerate(l):
        if c == '@':
            robot = (x*2, y)
        elif c == '#':
            walls.add((x*2,y))
            walls.add((x*2+1,y))
        elif c == 'O':
            boxes[boxNum] = [(x*2, y), (x*2+1, y)]
            boxMap[(x*2, y)] = boxNum
            boxMap[(x*2+1, y)] = boxNum
            boxNum += 1
    y += 1
    l = lines.pop(0)
height = y
#printMap()
moves = ""
while len(lines) > 0:
    l = lines.pop(0)
    moves += l
#print(data)
#print(moves)
counter = 0
for move in moves:
    np = getMove(robot, move)
    if np in walls:
        continue
    if np in boxMap:
        canMove, depBoxes = getBoxCanMove(boxMap[np], move)
        if not canMove:
            continue
        for box in depBoxes:
            moveBox(box, move)
    robot = np
    counter += 1
    print(f"Move: {move}, done {counter}")
    #printMap()
sumCoords = sum([box[0][1]*100+box[0][0] for box in boxes.values()])
print(f"Sum of boxes coordinates: {sumCoords}")








