from functools import reduce
from operator import concat

data = [int(l.removesuffix("\n")) for l in open("resources/day22_input.txt", "r")]

def getNextNumber(num):
    r = num*64
    num = num^r
    num = num % 16777216
    r = int(num/32)
    num = num^r
    num = num % 16777216
    r = num*2048
    num = num^r
    num = num % 16777216
    return num

randomNumbers = [[] for x in data]
sequences = [{} for x in data]
for pos,x in enumerate(data):
    randomNumbers[pos].append(x)
    for i in range(2000):
        x = getNextNumber(x)
        randomNumbers[pos].append(x)
        if i >= 3:
            seq = reduce(concat, [str(randomNumbers[pos][i+1-n]%10 - randomNumbers[pos][i-n]%10)+"," for n in (3,2,1,0)])
            if seq not in sequences[pos]:
                sequences[pos][seq] = x%10

res = sum(seq[2000] for seq in randomNumbers)
print(f"Sum of numbers: {res}")

allSequences = reduce(lambda a,b:a.union(b), [set(a.keys()) for a in sequences])
sumPrices = {}

for seqStr in allSequences:
    sumRes = sum([sequence[seqStr] for sequence in sequences if seqStr in sequence])
    sumPrices[seqStr] = sumRes

maxSum = max(sumPrices.values())
bestSeq = [a for a in sumPrices if sumPrices[a] == maxSum][0]
print(f"Best sequence: {bestSeq}, puchases {maxSum} bananas")



