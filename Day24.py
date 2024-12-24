import functools
import itertools
from itertools import combinations

DEBUG = True

def checkGate(gate):
    if wires[gate[3]][0] is not None:
        return
    if any( wires[gate[x]][0] is None for x in (1,2)):
        return None
    inA = wires[gate[1]][0]
    inB = wires[gate[2]][0]
    if gate[0] == 'AND':
        res = inA and inB
    elif gate[0] == 'OR':
        res = inA or inB
    elif gate[0] == 'XOR':
        res = inA != inB
    else:
        print("ERROR")
        exit(-1)
    wires[gate[3]][0] = res
    linkedGates = wires[gate[3]][1]
    for g in linkedGates:
        checkGate(g)

def resetWires():
    for w in wires:
        wires[w][0] = None

def runOnXY(x, y):
    resetWires()
    for bit in range(inWiresCount):
        bitStr = str(bit).zfill(2)
        xId = 'x'+bitStr
        yId = 'y'+bitStr
        xVal = False if x & 1 == 0 else True
        yVal = False if y & 1 == 0 else True
        wires[xId][0] = xVal
        wires[yId][0] = yVal
        for g in wires[xId][1]:
            checkGate(g)
        for g in wires[yId][1]:
            checkGate(g)


def buildTree(wire):
    gate = gates[wire]
    if gate[1][0] in ('x', 'y'):
        treeA = gate[1]
    else:
        treeA = buildTree(gate[1])
    if gate[2][0] in ('x', 'y'):
        treeB = gate[2]
    else:
        treeB = buildTree(gate[2])
    tree = (wire, gate[0], treeA, treeB)
    return tree

def printBranch(branch, pads=""):
    print(pads, branch[0], branch[1])
    newPads = "   " + pads
    order = (2,3)
    if not isinstance(branch[3], str):
        if isinstance(branch[3][2], str):
            order = (3,2)
    for i in order:
        if isinstance(branch[i], str):
            print(newPads, branch[i])
        else:
            printBranch(branch[i], newPads)

def isMainXor(branch, n):
    if n == 0:
        id = branch
        if not isinstance(branch, str):
            res = False
        else:
            res = branch[1:] == '00'
    else:
        id, op, a, b = branch
        if op != 'XOR':
            res =  False
        elif not isinstance(a, str) or not isinstance(b, str):
            res = False
        else:
            xn = 'x'+str(n).zfill(2)
            yn = 'y'+str(n).zfill(2)
            res = a == xn and b == yn or a == yn and b == xn
    #if not res and DEBUG:
    #    print(f"Branch {id} failed isMainXor level {n}")
    return res

def isMainAnd(branch, n):
    id, op, a, b = branch
    if op != 'AND':
        res = False
    elif not isinstance(a, str) or not isinstance(b, str):
        res = False
    else:
        xn = 'x'+str(n).zfill(2)
        yn = 'y'+str(n).zfill(2)
        res = a == xn and b == yn or a == yn and b == xn
    #if not res and DEBUG:
    #    print(f"Branch {id} failed isMainAnd level {n}")
    return res

def isCarryAnd(branch, n):
    # (XOR xNN-1 yNN-1     AND carryNN-2)
    id, op, a, b = branch
    if op != 'AND':
        res = False
    else:
        if isMainXor(a, n):
            res = isCarry(b, n)
        elif isMainXor(b, n):
            res = isCarry(a, n)
        else:
            res = False
    if not res and DEBUG:
        print(f"Branch {id} failed isCarryAnd level {n}")
    return res


def isCarry(branch, n):
    #carryNN = OR (AND xNN-1 yNN-1) or (XOR xNN-1 yNN-1 and carryNN-2)
    if n == 0:
        id = branch
        if not isinstance(branch, str):
            res = False
        else:
            res = branch[1:] == '00'
    else:
        id, op, a, b = branch
        if n == 1:
            res = isMainAnd(branch, n-1)
        elif op != 'OR':
            res = False
        elif isMainAnd(a, n-1):
            res = isCarryAnd(b, n-1)
        elif isMainAnd(b, n-1):
            res = isCarryAnd(a, n-1)
        else:
            res = False
    if not res and DEBUG:
        print(f"Branch {id} failed isCarry level {n}")
    return res

def checkIsAdder(branch):
    #zNN = XOR mainNN carryNN
    n = int(branch[0][1:])
    id, op, a, b = branch
    if op != 'XOR':
        res = False
    else:
        if isMainXor(a, n):
            res = isCarry(b, n)
        elif isMainXor(b,n):
            res = isCarry(a, n)
        else:
            res = False
    if not res and DEBUG:
        print(f"Branch {id} failed isAdder")
    return res

def swap(g1id, g2id):
    g1 = gates[g1id]
    g2 = gates[g2id]
    t = g1
    gates[g1id] = g2
    gates[g2id] = g1
    tId = g1id
    g1[3] = g2id
    g2[3] = tId
    print(f"Swapping {g2[3]},{g1[3]}")


lines = [l.removesuffix("\n") for l in open("resources/day24_input.txt", "r")]
wires = {}
gates = {}
l = lines.pop(0)
while l != "":
    id, valStr = l.split(": ")
    value = valStr == "1"
    wires[id] = [value, []]
    l = lines.pop(0)
inWiresCount = max(int(x[1:]) for x in wires)+1
while len(lines) > 0:
    l = lines.pop(0)
    gateStr, outWire = l.split(" -> ")
    inA, gateType, inB = gateStr.split(" ")
    gate = [gateType, inA, inB, outWire]
    for i in (inA, inB):
        if i not in wires:
            wires[i] = [None, [gate]]
        else:
            wires[i][1].append(gate)
    if outWire not in wires:
        wires[outWire] = [None, []]
    gates[outWire] = gate
    checkGate(gate)

resStr = ""
for w in sorted([x for x in wires if x[0] == 'z']):
    if wires[w][0] is None:
        print(f"Error None value of wire {w}")
        exit(-1)
    resStr = ('1' if wires[w][0] else '0') + resStr
resDec = int(resStr, 2)
print(f"Resulting number: {resDec}")

tree = {}
res = {}

allWs = sorted([x for x in wires if x[0] == 'z'])[:-1]
swaps = (('z08', 'mvb'),
        ('rds', 'jss'),
         ('z18', 'wss'),
         ('z23', 'bmn'))
for s in swaps:
    swap(s[0], s[1])

testW = 'z23x'
#g1id = 'rds'
#g2id = 'kdf'
res = True

for w in allWs:
    branch = buildTree(w)
    tree[w] = branch
    res = checkIsAdder(tree[w])
    #print(f"Testing {w}: {res[w]}")
    print(f"Testing {w}: {res}")
    if w == testW:
        printBranch(branch)
    if not res:
        break
if res:
    print("All passed")
    swapString = functools.reduce(lambda a,b: a+','+b, sorted(s for sw in swaps for s in sw))
    print(swapString)


