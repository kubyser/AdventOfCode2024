import itertools

lines = [l.removesuffix("\n") for l in open("resources/day8_input.txt", "r")]
width = len(lines[0])
height = len(lines)
#{'0': {(4, 4), (5, 2), (7, 3), (8, 1)}, 'A': {(8, 8), (6, 5), (9, 9)}}
nodes = {}
for y,l in enumerate(lines):
    for x,c in enumerate(l):
        if c!='.':
            if c in nodes:
                nodes[c].add((x,y))
            else:
                nodes[c] = {(x,y)}
antinodes = set()

PART2 = True

def diff_coords(a, b):
    return((a[0]-b[0], a[1]-b[1]))

def add_coords(start, diff, coeff=1):
    return tuple([start[coord] + diff[coord]*coeff for coord in (0,1)])

def check_bounds(p):
    return 0 <= p[0] < width and 0 <= p[1] < height

for t in nodes:
    for pair in itertools.combinations(nodes[t], 2):
        if not PART2:
            plist = [add_coords(pair[0], diff_coords(pair[1], pair[0]), x) for x in (2, -1)]
            for p in plist:
                if check_bounds(p):
                    antinodes.add(p)
        else:
            p = list(pair[0])
            antinodes.add(pair[0])
            for coeff in (1, -1):
                while True:
                    p = add_coords(p, diff_coords(pair[1], pair[0]), coeff)
                    if check_bounds(p):
                        antinodes.add(p)
                    else:
                        break
print(f"Number of antinodes: {len(antinodes)}")

