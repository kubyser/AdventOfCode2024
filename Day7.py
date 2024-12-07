data = {int(a.split(": ")[0]):[int(x) for x in a.split(": ")[1].split(" ")] for a in [l.removesuffix("\n") for l in open("resources/day7_input.txt", "r")]}
PART2 = True

def solve(test, eq):
    if len(eq) == 1:
        return eq[0] == test
    res = solve(test, [eq[0]+eq[1]] + eq[2:])
    if res:
        return True
    res = solve(test, [eq[0]*eq[1]] + eq[2:])
    if not PART2 or res:
        return res
    res = solve(test, [int(str(eq[0])+str(eq[1]))] + eq[2:])
    return res

sum_values = 0
for testvalue in data:
    nums = data[testvalue]
    res = solve(testvalue, nums)
    sum_values += testvalue if res else 0
print(f"Result: {sum_values}")

