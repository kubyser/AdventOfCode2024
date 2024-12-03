f = open("resources/day3_input.txt", "r")
data = [list(map(int, l.split(" "))) for l in f.read().splitlines()]
f.close()