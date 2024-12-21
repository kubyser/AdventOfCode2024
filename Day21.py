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

@functools.cache
def getSequence(targetSequence, keypad, startChar):
    pos = getCoords(keypad, startChar)
    sequence = ''
    for c in targetSequence:
        newPos = getCoords(keypad, c)
        if pos == newPos:
            sequence += 'A'
        elif newPos[1] == pos[1]:
            sequence += horSeq(keypad, pos, newPos) +'A'
        elif c in '<>' or c in '741' and pos[1]==3 or newPos[0]>pos[0] and (c in '235689' or c in '0A' and pos[0]!=0):
            sequence += vertSeq(keypad, pos, newPos) + horSeq(keypad, pos, newPos) + 'A'
        else:
            sequence += horSeq(keypad, pos, newPos) + vertSeq(keypad, pos, newPos) + 'A'
        pos = newPos
    return sequence


@functools.cache
def generateLength(c, prevC, depth):
    pos = getCoords(DIRECTIONAL_KEYPAD, prevC)
    sequence = ''
    newPos = getCoords(DIRECTIONAL_KEYPAD, c)
    if pos == newPos:
        sequence += 'A'
    elif newPos[1] == pos[1]:
        sequence += horSeq(DIRECTIONAL_KEYPAD, pos, newPos) +'A'
    elif c in '<>' or c in '741' and pos[1]==3 or newPos[0]>pos[0] and (c in '235689' or c in '0A' and pos[0]!=0):
        sequence += vertSeq(DIRECTIONAL_KEYPAD, pos, newPos) + horSeq(DIRECTIONAL_KEYPAD, pos, newPos) + 'A'
    else:
        sequence += horSeq(DIRECTIONAL_KEYPAD, pos, newPos) + vertSeq(DIRECTIONAL_KEYPAD, pos, newPos) + 'A'
    if depth == 1:
        #print(f"Char: {c}, depth={depth}, Full: {sequence}")
        return len(sequence)
    fullSequence = 0
    pc = 'A'
    for newChar in sequence:
        fullSequence += generateLength(newChar, pc, depth-1)
        pc = newChar
    #print(f"Char: {c}, depth={depth}, Full: {fullSequence}")
    return fullSequence


codes = [l.removesuffix("\n") for l in open("resources/day21_input.txt", "r")]
print(codes)
keypads = [NUMERIC_KEYPAD] + [DIRECTIONAL_KEYPAD]*25
finalSequences = []

for code in codes:
    #    positions = ['A']*len(keypads)
    targetSeq = getSequence(code, NUMERIC_KEYPAD, 'A')
    seq = 0
    print(f"target: {targetSeq}")
    pc = 'A'
    for c in targetSeq:
        seq += generateLength(c, pc, 25)
        pc = c
        #print(seq)
    print(f"Code: {code}, {seq}")
    finalSequences.append(seq)
score = [finalSequences[i]*int(codes[i].removesuffix('A')) for i in range(len(codes))]
print(f"Score: {sum(score)}")