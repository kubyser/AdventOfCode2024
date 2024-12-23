import itertools
from functools import reduce

def addOrCreate(key, value):
    if key not in data:
        data[key] = {value}
    else:
        data[key].add(value)

def hasLink(a, b):
    return a in data and b in data[a] or b in data and a in data[b]

def getHash(a, b, c):
    l = sorted([a,b,c])
    return str(l[0])+str(l[1])+str(l[2])

def bronKerbosch(r, p, x):
    global maxSet
    if len(p) == 0 and len(x) == 0 :
        if maxSet is None or len(r) > len(maxSet):
            maxSet = r.copy()
    while len(p) > 0:
        v = p.pop()
        res = bronKerbosch(r.union({v}), p.intersection(data[v]), x.intersection(data[v]))
        if res is not None:
            return res
        #p.remove(v)
        x.add(v)

lines = [l.removesuffix("\n") for l in open("resources/day23_input.txt", "r")]
data = {}
for l in lines:
    a,b = l.split('-')
    addOrCreate(a, b)
    addOrCreate(b, a)

threes = set()
for a in [d for d in data if d[0] == 't']:
    for (b, c) in itertools.combinations(data[a], 2):
        if c in data[b]:
            threes.add(getHash(a,b,c))
print(f"Threes: {len(threes)}")

maxSet = None
bronKerbosch(set(), set(data.keys()), set())
sm = reduce(lambda a,b: a +',' + b, sorted(list(maxSet)))
print(f"Password: {sm}")


