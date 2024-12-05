lines = [l.removesuffix("\n") for l in open("resources/day5_input.txt", "r")]
rules = {}
for l in lines[:lines.index("")]:
    r = [int(x) for x in l.split("|")]
    if r[1] in rules:
        rules[r[1]].add(r[0])
    else:
        rules[r[1]] = {r[0]}
print(rules)
sum_mid_updates = 0
sum_fixed_mid_updates = 0
for l in lines[lines.index("")+1:]:
    update = [int(x) for x in l.split(",")]
    printed = set()
    passed = True
    for page in update:
        printed.add(page)
        if page not in rules:
            continue
        if not all(x in printed for x in rules[page].intersection(update)):
            passed = False
            break
    if passed:
        sum_mid_updates += update[int(len(update)/2)]
    else:
        print(f"rule NOT ok: {l}")
        printed.clear()
        new_update = []
        lset = set(update)
        while len(update) > 0:
            for page in update:
                if all(p in printed for p in (set() if page not in rules else rules[page].intersection(lset))):
                    printed.add(page)
                    new_update.append(page)
                    update.remove(page)
                    break
        print(f"Fixed rule: {new_update}")
        sum_fixed_mid_updates += new_update[int(len(new_update)/2)]

print(f"Sum of middle pages: {sum_mid_updates}")
print(f"Sum of middle pages in fixed updates: {sum_fixed_mid_updates}")
