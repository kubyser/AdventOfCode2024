import re
from functools import reduce
from operator import concat, mul

data = "do()" + reduce(concat, open("resources/day3_input.txt", "r").readlines())
calculate = lambda program: sum(reduce(mul, map(int, l.split(","))) for l in re.findall(r'mul\((\d+,\d+)\)', program))
print(f"Part1: {calculate(data)}")
data = reduce(concat, [s[s.find("do()")+len("do()"):] for s in data.split("don\'t()") if "do()" in s])
print(f"Part2: {calculate(data)}")



