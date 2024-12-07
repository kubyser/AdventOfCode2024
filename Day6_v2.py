TURNS = {"N":"E", "E":"S", "S":"W", "W":"N"}
DIRECTIONS = {"N":(0,-1), "NE":(1,-1), "E":(1,0), "SE":(1,1), "S":(0,1), "SW":(-1,1), "W":(-1,0), "NW":(-1,-1)}

lines = [l.removesuffix("\n") for l in open("resources/day6_test_input.txt", "r")]
print(lines)
width = len(lines[0])
height = len(lines)
dataRows = {}
dataColumns = {}
data = set()
posX, posY = None, None
heading = "N"
for y,l in enumerate(lines):
    for x,c in enumerate(l):
        if c == "#":
            if y in dataRows:
                dataRows[y].add(x)
            else:
                dataRows[y] = {x}
            if x in dataColumns:
                dataColumns[x].add(y)
            else:
                dataColumns[x] = {y}
            data.add((x,y))
        elif c == '^':
            posX, posY = x, y
print(dataColumns, dataRows, posX, posY)
visited = set()
while True:
    visited.add((posX, posY))
    newPosX = posX+DIRECTIONS[heading][0]
    newPosY = posY+DIRECTIONS[heading][1]
    if newPosX < 0 or newPosX >= width or newPosY < 0 or newPosY >= height:
        break
    if (newPosX, newPosY) in data:
        heading = TURNS[heading]
    else:
        posX = newPosX
        posY = newPosY
print(f"Visited: {len(visited)}")
exit(0)

obst = []
if heading == "N":
    obst = [n for n in dataColumns[posX] if n < posY] if posX in dataColumns else []
elif heading == "S":
    obst = [n for n in dataColumns[posX] if n > posY] if posX in dataColumns else []
elif heading == "W":
    obst = [n for n in dataRows[posY] if n < posX] if posY in dataRows else []
elif heading == "E":
    obst = [n for n in dataRows[posY] if n > posX] if posY in dataRows else []
else:
    exit(-1)
if len(obst) == 0:
    if heading == "N":
        numVisited += posY
    elif heading == "S":
        numVisited += height-posY-1
    elif heading == "W":
        numVisited += posX
    elif heading == "E":
        numVisited += width-posX-1
    else:
        exit(-1)
    break
if heading == "N":
    newPosY = max(obst)
    numVisited += abs(posY - newPosY)
    posY = newPosY
elif heading == "S":
    newPosY = min(obst)
    numVisited += abs(posY - newPosY)
    posY = newPosY
elif heading == "W":
    newPosX = max(obst)
    numVisited += abs(posX - newPosX)
    posX = newPosX
elif heading == "E":
    newPosX = min(obst)
    numVisited += abs(posX - newPosX)
    posX = newPosX
else:
    exit(-1)
heading = TURNS[heading]
print(numVisited)