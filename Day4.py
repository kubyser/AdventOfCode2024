import itertools
from functools import reduce
from operator import concat

data = [l.removesuffix("\n") for l in open("resources/day4_input.txt", "r")]
width = len(data[0])
height = len(data)

DIRECTIONS = {"N":(0,-1), "NE":(1,-1), "E":(1,0), "SE":(1,1), "S":(0,1), "SW":(-1,1), "W":(-1,0), "NW":(-1,-1)}
getWordByDxDy = lambda data, x, y, dx, dy, length: reduce(concat,[data[y][x] for x,y in zip([x]*length if dx==0 else range(x, min(len(data[y]), max(-1, x+dx*length)), dx),
                                                                      [y]*length if dy==0 else range(y, min(len(data), max(-1, y+dy*length)), dy))])
getWordByDirection = lambda data, x, y, direction, length: getWordByDxDy(data, x, y, DIRECTIONS[direction][0], DIRECTIONS[direction][1], length)

WORD = 'XMAS'
res = sum([getWordByDirection(data, x, y, d, len(WORD)) == WORD for d in DIRECTIONS for x, y in list(itertools.product(range(width), range(height))) if data[y][x] == WORD[0]])
print("Count of XMAS: ", res)

WORD = 'MAS'
res = sum([(getWordByDirection(data, x-1, y-1, "SE", len(WORD)) in (WORD, WORD[::-1]) and
            getWordByDirection(data, x-1, y+1, "NE", len(WORD)) in (WORD, WORD[::-1]))
           for x, y in list(itertools.product(range(1, width-1), range(1, height-1)))
                        if data[y][x] == WORD[1]])
print("Count of X-MAS: ", res)


