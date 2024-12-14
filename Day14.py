from functools import reduce
from operator import mul

def printRobots(output = None):
    for y in range(size[1]):
        s = ""
        for x in range(size[0]):
            if (x,y) in tiles:
                s += str(len(tiles[(x,y)]))
            else:
                s += "."
        if output is None:
            print(s)
        else:
            output.write(s+"\n")

def hashRobots():
    s = ""
    for y in range(size[1]):
        for x in range(size[0]):
            if (x,y) in tiles:
                s += str((x, y)) + str(tiles[(x,y)])
    return(s)

def solvePart1():
    counter = 100
    for id in robots:
        robot = robots[id]
        pos = [(robot[0][x] + robot[1][x]*counter) % size[x] for x in (0,1)]
        robot[0][0] = pos[0]
        robot[0][1] = pos[1]
        tiles.add(tuple(pos))
        quadrant = tuple([0 if pos[x] < int(size[x]/2) else 1 if pos[x] > int(size[x]/2) else None for x in (0,1)])
        if all(x is not None for x in quadrant):
            if quadrant not in robotsInQuadrants:
                robotsInQuadrants[quadrant] = 1
            else:
                robotsInQuadrants[quadrant] += 1
    res = reduce(mul, robotsInQuadrants.values())
    return res

lines = [l.removesuffix("\n") for l in open("resources/day14_input.txt", "r")]
robots = {}
tiles = {}
id = 0
size = [0, 0]
for l in lines:
    pos = [int(x) for x in l.split(" ")[0].removeprefix("p=").split(",")]
    if pos[0]+1 > size[0]:
        size[0] = pos[0]+1
    if pos[1]+1 > size[1]:
        size[1] = pos[1]+1
    speed = [int(x) for x in l.split(" ")[1].removeprefix("v=").split(",")]
    robots[id] = [pos, speed]
    id += 1
#print(size, robots)
PART2 = True

if not PART2:
    print(f"Part1 answer: {solvePart1()}")
    exit(0)

counter = 0
robotsInQuadrants = {}
cache = {}
output = open("resources/day14_output1.txt", "w")
while True:
    tiles.clear()
    robotsInQuadrants.clear()
    for id in robots:
        robot = robots[id]
        pos = tuple([(robot[0][x] + robot[1][x]) % size[x] for x in (0,1)])
        robot[0][0] = pos[0]
        robot[0][1] = pos[1]
        if pos not in tiles:
            tiles[pos] = {id}
        else:
            tiles[pos].add(id)
        quadrant = tuple([0 if pos[x] < int(size[x]/2) else 1 if pos[x] > int(size[x]/2) else None for x in (0,1)])
        if all(x is not None for x in quadrant):
            if quadrant not in robotsInQuadrants:
                robotsInQuadrants[quadrant] = 1
            else:
                robotsInQuadrants[quadrant] += 1

    #if robotsInQuadrants[(0,0)] == robotsInQuadrants[(1,0)] and robotsInQuadrants[(0,1)] == robotsInQuadrants[(1,1)]:
    if (counter-22) % size[0] == 0:
        printRobots(output)
        #print(robotsInQuadrants)
        h = hashRobots()
        #print(f"Seconds = {counter+1}")
        output.write("Seconds = " + str(counter+1)+"\n")
        if h not in cache:
            cache[h] = counter
        else:
            print(f"Already see at step {cache[h]}")
            output.close()
            exit(0)
        #print(hashRobots())
        #a = input("Say something")
    counter += 1

exit(0)



