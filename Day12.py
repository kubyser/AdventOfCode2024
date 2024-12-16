import aoc
data = [l.removesuffix("\n") for l in open("resources/day12_input.txt", "r")]
width = len(data[0])
height = len(data)
#print(data)

AREA = "AREA"
PERIMETER = "PERIMETER"
SIDES = "SIDES"
TYPE = "TYPE"
PLOTS = "PLOTS"

def check_bounds(x, y):
    return 0 <= x < width and 0 <= y < height

visited = set()
reginfo = {}
regnum = 0
for y,l in enumerate(data):
    for x,c in enumerate(l):
        if (x,y) in visited:
            continue
        regnum += 1
        regtype = data[y][x]
        reginfo[regnum] = {AREA: 0, PERIMETER: 0, SIDES: 0, TYPE: regtype, PLOTS: {}}
        to_explore = {(x,y)}
        while len(to_explore) > 0:
            (cx,cy) = to_explore.pop()
            visited.add((cx,cy))
            reginfo[regnum][AREA] += 1
            reginfo[regnum][PLOTS][cx, cy] = set()
            for direction in ["N", "S", "E", "W"]:
                nx, ny = aoc.addCoords((cx,cy), aoc.DIRECTION_MOVEMENT[direction])
                if check_bounds(nx, ny) and data[ny][nx] == regtype:
                    if (nx, ny) not in visited:
                        to_explore.add((nx, ny))
                else:
                    reginfo[regnum][PERIMETER] += 1
                    reginfo[regnum][PLOTS][cx, cy].add(direction)
cost = sum([reginfo[r][AREA]*reginfo[r][PERIMETER] for r in reginfo])
print(f"Cost of fence part 1: {cost}")
dirs_to_check = {"N": ("E","W"), "S": ("E","W"), "E": ("N","S"), "W": ("N","S")}
for regtype in reginfo:
    plots = reginfo[regtype][PLOTS]
    for (x,y) in plots:
        for dir in dirs_to_check:
            if dir in plots[x,y]:
                nx, ny = aoc.addCoords((x,y), aoc.DIRECTION_MOVEMENT[dirs_to_check[dir][0]])
                if not check_bounds(nx, ny) or (nx,ny) not in plots or dir not in plots[nx, ny]:
                    reginfo[regtype][SIDES] += 1
#print(reginfo)
cost = sum([reginfo[r][AREA]*reginfo[r][SIDES] for r in reginfo])
print(f"Cost of fence part 2: {cost}")

