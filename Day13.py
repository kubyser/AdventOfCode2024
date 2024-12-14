lines = [l.removesuffix("\n") for l in open("resources/day13_input.txt", "r")]
arcades = []
PART2 = True
while len(lines) > 0:
    line = lines.pop(0)
    if line == "":
        continue
    line = line.removeprefix("Button A: X+").replace(" Y+", "").split(",")
    ax, ay = int(line[0]), int(line[1])
    line = lines.pop(0)
    line = line.removeprefix("Button B: X+").replace(" Y+", "").split(",")
    bx, by = int(line[0]), int(line[1])
    line = lines.pop(0)
    line = line.removeprefix("Prize: X=").replace(" Y=", "").split(",")
    px, py = int(line[0]) + (10000000000000 if PART2 else 0), int(line[1]) + (10000000000000 if PART2 else 0)
    arcade = [(ax,ay), (bx,by), (px,py)]
    arcades.append(arcade)
best = []
# [0][0] [1][0] [2][0]
# [0][1] [1][1] [2][1]
for arcade in arcades:
    det = arcade[0][0]*arcade[1][1] - arcade[1][0]*arcade[0][1]
    detA = arcade[2][0]*arcade[1][1] - arcade[1][0]*arcade[2][1]
    detB = arcade[0][0]*arcade[2][1] - arcade[2][0]*arcade[0][1]
    a = detA / det
    b = detB / det
    if int(a) == a and int(b) == b:
        best.append((int(a), int(b)))
res = sum(a*3+b for a,b in best)
print(f"Minimal tokens: {res}")

