def checkReport(report, toSkip = None):
    rep = report if toSkip is None else report[:toSkip] + report[toSkip+1:]
    diffs = list(map(lambda x,y: y-x, rep, rep[1:]))
    return all([x in [1,2,3] for x in diffs]) or all([x in [-3,-2,-1] for x in diffs])

data = [[int(n) for n in l.split()] for l in open("resources/day2_input.txt", "r")]
safe_reports_part_1 = sum([checkReport(report) for report in data])
print(f"safe reports part 1: {safe_reports_part_1}")
safe_reports_part_2 = sum([checkReport(report) or any([checkReport(report, skip) for skip,r in enumerate(report)]) for report in data])
print(f"safe reports part 2: {safe_reports_part_2}")