def checkReport(report, toSkip = None):
    rep = report if toSkip is None else report[:toSkip] + report[toSkip+1:]
    diffs = [rep[i+1]-rep[i] for i,j in list(enumerate(rep))[:-1]]
    return all([x in range(1,4) for x in diffs]) or all([x in range(-3,0) for x in diffs])

f = open("resources/day2_input.txt", "r")
data = [list(map(int, l.split(" "))) for l in f.read().splitlines()]
f.close()
safe_reports_part_1 = sum([1 if checkReport(report) else 0 for report in data])
print("safe reports part 1: ", safe_reports_part_1)
safe_reports_part_2 = sum([1 if any([checkReport(report, skip) for skip in [None] + [x for x,y in enumerate(report)]]) else 0 for report in data])
print("safe reports part 2: ", safe_reports_part_2)

