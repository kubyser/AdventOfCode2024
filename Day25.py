lines = [l.removesuffix("\n") for l in open("resources/day25_input.txt", "r")]
locks = []
keys = []
while len(lines) > 0:
    l = lines.pop(0)
    if l == '':
        continue
    if l == '#####':
        lockMode = True
        lock = [None]*5
    else:
        lockMode = False
        key = [None]*5

    for i in range(6):
        l = lines.pop(0)
        for j in range(5):
            if lockMode:
                if l[j] == '.' and lock[j] is None:
                    lock[j] = i
            else:
                if l[j] == '#' and key[j] is None:
                    key[j] = 5-i
    if lockMode:
        locks.append(lock)
    else:
        keys.append(key)

#print(locks)
#print(keys)

fitCount = 0
for lock in locks:
    for key in keys:
        fit = all(sum(x)<=5 for x in zip(lock, key))
        fitCount += 1 if fit else 0

print(f"Lock/key combinations that fit: {fitCount}")




