instr = [l.removesuffix("\n") for l in open("resources/day9_input.txt", "r")][0]
disk = []
modeFile = True
id = 0
free = []
files = {}
pos = 0
for c in instr:
    n = int(c)
    if modeFile:
        disk += [id]*n
        files[id] = (pos, n)
        id += 1
    else:
        disk += [-1]*n
        free.append((pos, n))
    pos += n
    modeFile = not modeFile
print(files, free)
curId = max(files)
while curId >= 0:
    curPos, size = files[curId]
    for i, (p, n) in enumerate(free):
        if p<curPos and n>=size:
            files[curId] = (p, size)
            if n > size:
                free[i] = (p+size, n-size)
            else:
                free.pop(i)
            break
    curId -= 1
print(files, free)
checkSum = 0
for id in files:
    p,n = files[id]
    checkSum += sum([id*pos for pos in range(p, p+n)])
print(f"Checksum: {checkSum}")


exit(0)
posFirst = 0
posLast = len(disk)-1
while posFirst<posLast:
    if disk[posLast] == -1:
        posLast -= 1
        continue
    if disk[posFirst] != -1:
        posFirst += 1
        continue
    disk[posFirst] = disk[posLast]
    disk[posLast] = -1
    posFirst += 1
    posLast -= 1
print(disk)
checkSum = sum([x*p for p, x in enumerate(disk) if x != -1])
print(f"Checksum: {checkSum}")



