TURNS = {"N":"E", "E":"S", "S":"W", "W":"N"}
DIRECTIONS = {"N":(0,-1), "NE":(1,-1), "E":(1,0), "SE":(1,1), "S":(0,1), "SW":(-1,1), "W":(-1,0), "NW":(-1,-1)}

lines = [l.removesuffix("\n") for l in open("resources/day6_input.txt", "r")]
width = len(lines[0])
height = len(lines)
data = set()
posX, posY = None, None
heading = "N"
for y,l in enumerate(lines):
    for x,c in enumerate(l):
        if c == "#":
            data.add((x,y))
        elif c == '^':
            posX, posY = x, y
visited = set()
startX = posX
startY = posY
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
real_visited = visited.copy()
goodNewObstacles = set()
for y in range(height):
    for x in range(width):
        if (x, y) in data or (x == startX and y == startY) or (x, y) not in real_visited:
            continue
        visited = set()
        posX = startX
        posY = startY
        heading = "N"
        while True:
            if (posX, posY, heading) in visited:
                #print("Loop detected!")
                goodNewObstacles.add((x, y))
                break
            visited.add((posX, posY, heading))
            newPosX = posX+DIRECTIONS[heading][0]
            newPosY = posY+DIRECTIONS[heading][1]
            if newPosX < 0 or newPosX >= width or newPosY < 0 or newPosY >= height:
                break
            if (newPosX, newPosY) in data or (newPosX, newPosY) == (x, y):
                heading = TURNS[heading]
            else:
                posX = newPosX
                posY = newPosY
print(f"Possible new obstacles: {len(goodNewObstacles)}")