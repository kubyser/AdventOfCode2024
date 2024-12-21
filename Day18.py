from aoc import addCoords, DIRECTION_MOVEMENT, DIRECTIONS_MAIN

def check_bounds(pos):
    return 0 <= pos[0] <= width and 0 <= pos[1] <= height

def findPath():
    to_visit = {start:0}
    visited = {}
    while len(to_visit) > 0:
        steps = min(x for x in to_visit.values())
        pos = [p for p in to_visit if to_visit[p]==steps][0]
        to_visit.pop(pos)
        if pos in visited:
            if visited[pos] < steps:
                continue
        visited[pos] = steps
        if pos == end:
            break
        nextMoves = [addCoords(pos, DIRECTION_MOVEMENT[d]) for d in DIRECTIONS_MAIN]
        nextSteps = steps+1
        for nextPos in nextMoves:
            if check_bounds(nextPos) and nextPos not in data and (nextPos not in to_visit or to_visit[nextPos]>nextSteps):
                to_visit[nextPos] = nextSteps
    if end in visited:
        return visited[end]
    else:
        return None


lines = [l.removesuffix("\n") for l in open("resources/day18_input.txt", "r")]
MAXTIME = 1024
blocks = [[int(a) for a in l.split(",")] for l in lines]
width = max([a[0] for a in blocks])
height = max([a[1] for a in blocks])
print(width, height, blocks)
data = {}
for i in range(MAXTIME):
    #timeBlock = (tuple(blocks[i]), i)
    data[tuple(blocks[i])] = i
print(data)
start = (0,0)
end = (width, height)
bestTime = findPath()
print(f"Minimum steps: {bestTime}")
time = MAXTIME
while True:
    block = blocks[time]
    data[tuple(blocks[time])] = time
    path = findPath()
    if path is None:
        print(f"Found: {block}")
        break
    time += 1

