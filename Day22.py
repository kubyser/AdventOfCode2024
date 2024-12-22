import time
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

def shiftLeft(a):
    for i in range(len(a)-1):
        curSeq[i] = curSeq[i+1]


startTime = time.time()
lastRandomNumbers = [None]*len(data)
sequences = [{} for x in data]
for pos,prevX in enumerate(data):
    curSeq = [None]*4
    #randomNumbers[pos].append(x)
    curSeq[3] = prevX%10
    x = None
    for i in range(2000):
        x = getNextNumber(prevX)
        shiftLeft(curSeq)
        curSeq[3] = x%10-prevX%10
        #randomNumbers[pos].append(x)
        if i >= 3:
            seq = reduce(concat, [str(n)+"," for n in curSeq])
            if seq not in sequences[pos]:
                sequences[pos][seq] = x%10
        prevX = x
    lastRandomNumbers[pos] = x

res = sum(lastRandomNumbers)
endTime = time.time()
print(f"Sum of numbers: {res}")
print(f"Time elapsed: {endTime-startTime}")

allSequences = reduce(lambda a,b:a.union(b), [set(a.keys()) for a in sequences])
sumPrices = {}

for seqStr in allSequences:
    sumRes = sum([sequence[seqStr] for sequence in sequences if seqStr in sequence])
    sumPrices[seqStr] = sumRes

maxSum = max(sumPrices.values())
bestSeq = [a for a in sumPrices if sumPrices[a] == maxSum][0]
endTime = time.time()
print(f"Best sequence: {bestSeq}, puchases {maxSum} bananas")
print(f"Time elapsed: {endTime-startTime}")



