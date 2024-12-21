import functools

NUMERIC_KEYPAD = ('789','456','123',' 0A')
DIRECTIONAL_KEYPAD = (' ^A', '<v>')

def getCoords(keypad, c):
    for i,s in enumerate(keypad):
        if c in s:
            return s.find(c),i

def horSeq(keypad, startPos, endPos):
    return ('>' if endPos[0]>startPos[0] else '<')* abs(endPos[0]-startPos[0])

def vertSeq(keypad, startPos, endPos):
    return ('v' if endPos[1]>startPos[1] else '^')* abs(endPos[1]-startPos[1])

def getMovementSequence(oldPos, newPos, keypad):
    c = keypad[oldPos[1]][oldPos[0]]
    if oldPos == newPos:
        return 'A'
    elif newPos[1] == oldPos[1]:
        return horSeq(keypad, oldPos, newPos) +'A'
    elif c in '<>' or c in '741' and oldPos[1]==3 or newPos[0]>oldPos[0] and (c in '235689' or c in '0A' and oldPos[0]!=0):
        return vertSeq(keypad, oldPos, newPos) + horSeq(keypad, oldPos, newPos) + 'A'
    else:
        return horSeq(keypad, oldPos, newPos) + vertSeq(keypad, oldPos, newPos) + 'A'


def getSequence(targetSequence, keypad, startChar):
    pos = getCoords(keypad, startChar)
    sequence = ''
    for c in targetSequence:
        newPos = getCoords(keypad, c)
        sequence += getMovementSequence(pos, newPos, keypad)
        pos = newPos
    return sequence


@functools.cache
def generateLength(c, prevC, depth, keypad):
    pos = getCoords(DIRECTIONAL_KEYPAD, prevC)
    sequence = ''
    newPos = getCoords(DIRECTIONAL_KEYPAD, c)
    sequence += getMovementSequence(pos, newPos, DIRECTIONAL_KEYPAD)
    if depth == 1:
        #print(f"Char: {c}, depth={depth}, Full: {sequence}")
        return len(sequence)
    fullSequence = 0
    pc = 'A'
    for newChar in sequence:
        fullSequence += generateLength(newChar, pc, depth-1, DIRECTIONAL_KEYPAD)
        pc = newChar
    #print(f"Char: {c}, depth={depth}, Full: {fullSequence}")
    return fullSequence


codes = [l.removesuffix("\n") for l in open("resources/day21_input.txt", "r")]
print(codes)
keypads = [NUMERIC_KEYPAD] + [DIRECTIONAL_KEYPAD]*25
finalSequences = []

def troubleshoot():
    for seq in ['<^A', '^<A', '>vA', 'v>A']:
        res = seq + ' (' + str(len(seq)) + ')'
        for i in range(2):
            seq = getSequence(seq, DIRECTIONAL_KEYPAD, 'A')
            res += '  ->  ' + seq + ' (' + str(len(seq)) + ')'
        print(res)
    exit(0)

#troubleshoot()

NUM_NUMPADS = 25
for code in codes:
    #    positions = ['A']*len(keypads)
    targetSeq = getSequence(code, NUMERIC_KEYPAD, 'A')
    seq = 0
    pc = 'A'
    for c in targetSeq:
        seq += generateLength(c, pc, NUM_NUMPADS, DIRECTIONAL_KEYPAD)
        pc = c
    print(f"Code: {code}, {seq}")
    finalSequences.append(seq)
score = [finalSequences[i]*int(codes[i].removesuffix('A')) for i in range(len(codes))]
print(f"Final score: {sum(score)}")