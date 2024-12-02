f = open("resources/day1_input.txt", "r")
lines = [list(map(int, x)) for x in [l.split("  ") for l in f.read().splitlines()]]
f.close()
a = sorted([x[0] for x in lines])
b = sorted([x[1] for x in lines])
m = {x:b.count(x) for x in b}
dist = sum([abs(x[0] - x[1]) for x in zip(a, b)])
sim = sum(x*m[x] for x in a if x in b)
print(dist, sim)