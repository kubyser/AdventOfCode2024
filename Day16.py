from functools import reduce
from aoc import DIRECTION_MOVEMENT, TURNS, addCoords, stringsArrayToLists, DIRECTIONS_MAIN

def getMaze(coords):
    return maze[coords[1]][coords[0]]

def printMap():
    for y in range(height):
        s = ""
        for x in range(width):
            s += "o" if (x,y) in pathTiles else "x" if any([((x,y), d) in visited for d in ("N","S","E","W")]) else getMaze((x,y))
        print(s)

SCORE = "SCORE"
PATH = "PATH"

lines = [l.removesuffix("\n") for l in open("resources/day16_input.txt", "r")]
maze, height, width = stringsArrayToLists(lines, lambda c: c if c not in ('S', 'E') else '.')
start = (1, height-2)
end = (width-2, 1)

pos = (start, 'E')
visited = {}
to_visit = {pos: {SCORE: 0, PATH: {start}}}
while len(to_visit) > 0:
    minscore = min(x[SCORE] for x in to_visit.values())
    pos = [p for p in to_visit if to_visit[p][SCORE]==minscore][0]
    path = to_visit[pos][PATH]
    to_visit.pop(pos)
    if pos in visited:
        if visited[pos][SCORE] < minscore:
            continue
        if visited[pos][SCORE] == minscore:
            newPath = visited[pos][PATH].union(path)
            visited[pos] = {SCORE:minscore, PATH: newPath}
            continue
    visited[pos] = {SCORE:minscore, PATH: path}
    if pos[0] == end:
        break
    #print(f"POS: {pos}, TO_VISIT: {to_visit}")
    nextMove = [((addCoords(pos[0], DIRECTION_MOVEMENT[pos[1]]), pos[1]), minscore + 1),
                ((addCoords(pos[0], DIRECTION_MOVEMENT[TURNS[pos[1]]["L"]]), TURNS[pos[1]]["L"]), minscore + 1000 + 1),
                ((addCoords(pos[0], DIRECTION_MOVEMENT[TURNS[pos[1]]["R"]]), TURNS[pos[1]]["R"]), minscore + 1000 + 1)]
    for newPos, newScore in nextMove:
        if getMaze(newPos[0]) != '#':
            newPath = path.union({newPos[0]})
            if newPos in to_visit and to_visit[newPos][SCORE]==newScore:
                newPath = newPath.union((to_visit[newPos][PATH]))
            if newPos not in to_visit or to_visit[newPos][SCORE]>=newScore:
                to_visit[newPos] = {SCORE: newScore, PATH: newPath}
#printMap()
bestScore = min([visited[key][SCORE] for key in visited.keys() if key[0]==end])
pathTiles = reduce(lambda a,b: a.union(b), [visited[key][PATH] for key in visited.keys() if key[0]==end and visited[key][SCORE] == bestScore])
print(f"Minimal score:{bestScore}, tiles = {len(pathTiles)}")





