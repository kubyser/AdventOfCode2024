lines = [l.removesuffix("\n") for l in open("resources/day13_test_input.txt", "r")]
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
print(arcades)
best = []
for arcade in arcades:
    for b_pushes in range(101):
        remX = arcade[2][0]-arcade[1][0]*b_pushes
        remY = arcade[2][1]-arcade[1][1]*b_pushes
        if remX==0 and remY==0:
            best.append((0, b_pushes))
            break
        if remX<0 or remY<0:
            break
        if remX % arcade[0][0] != 0 or remY % arcade[0][1] != 0:
            continue
        a_pushes = int(remX / arcade[0][0])
        if a_pushes * arcade[0][1] != remY:
            continue
        best.append((a_pushes, b_pushes))
        break
res = sum(a*3+b for a,b in best)
print(f"Minimal tokens: {res}")

