import functools

lines = [l.removesuffix("\n") for l in open("resources/day19_input.txt", "r")]
patterns = lines[0].split(", ")
designs = lines[2:]
#print(patterns, designs)
maxPatternLength = max([len(s) for s in patterns])

@functools.cache
def checkDesign(design):
    combinations = 0
    for patLength in range(1, min(maxPatternLength+1, len(design)+1)):
        seq = design[:patLength]
        if seq in patterns:
            if patLength == len(design):
                combinations += 1
            else:
                passed = checkDesign(design[patLength:])
                if passed:
                    combinations += passed
    return combinations


numPossible = 0
numCombinations = 0
for i, design in enumerate(designs):
    print(f"Checking {i} of {len(designs)}: {design}")
    checkResult = checkDesign(design)
    print(f"Result of check: {checkResult}")
    numPossible += 1 if checkResult else 0
    numCombinations += checkResult

print(f"Possible designs: {numPossible}")
print(f"Possible combinations: {numCombinations}")

