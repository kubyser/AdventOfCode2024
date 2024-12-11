import aoc
from aoc import DIRECTIONS

lines = [l.removesuffix("\n") for l in open("resources/day10_input.txt", "r")]
data, height, width = aoc.stringsArrayToLists(lines, int)

def check_bounds(x, y):
    return 0 <= x < width and 0 <= y < height

def explore(x, y, path, part2=False):
    global data
    newpath = path + str(x)+","+str(y)+"-" if part2 else str(x)+","+str(y)
    if data[y][x] == 9:
        return {newpath}
    all_reachable = set()
    for dir in ["N", "E", "S", "W"]:
        nx = x + DIRECTIONS[dir][0]
        ny = y + DIRECTIONS[dir][1]
        if check_bounds(nx, ny):
            if data[ny][nx] == data[y][x]+1:
                reachable = explore(nx, ny, newpath, part2)
                all_reachable = all_reachable.union(reachable)
    return all_reachable

for PART2 in (False, True):
    sum_scores = sum([len(explore(x, y, "", PART2)) for y in range(height) for x in range(width) if data[y][x] == 0])
    print(f"Sum of scores for part {'2' if PART2 else '1'}: {sum_scores}")



