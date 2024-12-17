import math
from functools import reduce
from operator import concat

A = 0
B = 1
C = 2

outputString = ""

def combo(op):
    if op in [0,1,2,3]:
        return op
    if op in [4,5,6]:
        return registers[op-4]
    if op == 7:
        print("ERROR! op=7")
        return None
    return None

def execute(opcode, operand):
    global outputString
    if opcode == 0:
        registers[A] = int(registers[A] / (2 ** combo(operand)))
    elif opcode == 1:
        registers[B] = registers[B]^operand
    elif opcode == 2:
        registers[B] = combo(operand) % 8
    elif opcode == 3:
        if registers[A] != 0:
            return operand
    elif opcode == 4:
        registers[B] = registers[B] ^ registers[C]
    elif opcode == 5:
        res = str(combo(operand) % 8)
        #print(res)
        outputString += res + ","

    elif opcode == 6:
        registers[B] = int(registers[A] / (2 ** combo(operand)))
    elif opcode == 7:
        registers[C] = int(registers[A] / (2 ** combo(operand)))
    else:
        print(f"ERROR! invalid opcode {opcode}")
        exit(-1)
    return None

def run(program):
    global outputString
    pointer = 0
    outputString = ""
    while pointer < len(program):
        opcode = program[pointer]
        operand = program[pointer+1]
        res = execute(opcode, operand)
        if res is not None:
            pointer = res
        else:
            pointer += 2


lines = [l.removesuffix("\n") for l in open("resources/day17_input.txt", "r")]
registers = [0]*3
initregisters = [0]*3
l = lines.pop(0)
registers[A] = int(l.split(": ")[1])
l = lines.pop(0)
registers[B] = int(l.split(": ")[1])
l = lines.pop(0)
registers[C] = int(l.split(": ")[1])
lines.pop(0)
l = lines.pop(0)
programString = l.split(": ")[1]
program = [int(x) for x in l.split(": ")[1].split(",")]
initProgram = program.copy()

def findProg(digits, pos):
    global registers
    d = digits.copy()
    for i in range(8):
        if i==0 and pos==0:
            continue
        d[pos] = i
        aoct = reduce(concat, [str(x) for x in d])
        avalue = int(aoct, 8)
        registers = [avalue, initregisters[B], initregisters[C]]
        run(program)
        mydigit = int(outputString.split(",")[15-pos])
        wanted = initProgram[15-pos]
        print(aoct, "{0:b}".format(avalue), outputString)
        if mydigit == wanted:
#            print(aoct, "{0:b}".format(avalue), outputString)
            if pos == 15:
                return avalue
            res = findProg(d, pos+1)
            if res is not None:
                return res
    return None


#registers = [0,2024,43690]
#program = [4,0]
avalue = 2**48
abin = [0]*16
abin[0] = 1
#abin[16] = 0b110

res = findProg(abin, 0)
print(programString)
print(res)
exit(0)

print(f"A: {avalue}, Result: {outputString}")
