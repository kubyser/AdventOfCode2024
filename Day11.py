import functools
import operator

def incdict(dict, key, value=1):
    if key in dict:
        dict[key] += value
    else:
        dict[key] = value

line = [l.removesuffix("\n") for l in open("resources/day11_input.txt", "r")][0]
print(line)
data = {int(s): line.split(" ").count(s) for s in line.split(" ")}
counter = 0
while True:
    counter += 1
    newdata = {}
    for x in data:
        numx = data[x]
        if x == 0:
            incdict(newdata, 1, numx)
        elif len(str(x))%2 == 0:
            a, b = int(str(x)[:int(len(str(x))/2)]), int(str(x)[int(len(str(x))/2):])
            incdict(newdata, a, numx)
            incdict(newdata, b, numx)
        else:
            incdict(newdata, x*2024,  numx)
    data = newdata
    if counter in [25, 75]:
        numstones = sum(data.values())
        print(f"Number of stones after {counter} blinks: {numstones}")
        if counter == 75:
            break
