import aoc

lines = [l.removesuffix("\n") for l in open("resources/day20_input.txt", "r")]
width = len(lines[0])
height = len(lines)
data = [[None for x in range(width)] for y in range(height)]
start = None
end = None
for y,l in enumerate(lines):
    for x,c in enumerate(l):
        data[y][x] = c
        if c == 'S':
            start = (x,y)
        elif c == 'E':
            end = (x,y)
#print(start,end, data)
pos = start
path = {}
to_visit = {(start,0)}
while len(to_visit)>0:
    pos, time = to_visit.pop()
    path[pos] = time
    if pos == end:
        break
    nextMoves = [aoc.addCoords(pos, aoc.DIRECTION_MOVEMENT[d]) for d in aoc.DIRECTIONS_MAIN]
    for nextPos in nextMoves:
        if nextPos not in path and data[nextPos[1]][nextPos[0]] != '#':
            to_visit.add((nextPos, time+1))

bestTime = path[end]
print(f"Best time before cheat: {bestTime}")

cheats = {}

CHEAT_DURATION = 20

for pos in path:
    time = path[pos]
    nextPositions = [x for x in path if path[x]>time]
    for np in nextPositions:
        cheatTime = abs(np[0]-pos[0]) + abs(np[1]-pos[1])
        savedTime = path[np] - time - cheatTime
        if cheatTime <= CHEAT_DURATION and savedTime > 0:
            cheats[(pos, np)] = savedTime

#for l in range(len(path)):
#    ch = [c for c in cheats if cheats[c] == l]
#    if len(ch) > 0:
#        print(f"{len(ch)} cheats save {l}")
ch = [c for c in cheats if cheats[c] >= 100]
print(f"{len(ch)} cheats save at least 100")





