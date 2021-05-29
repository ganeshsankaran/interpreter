from errors import *
from handlers import *
import sys

# read program
with open(sys.argv[1], 'r') as f:
    text = f.read()
    instrs = text.split('\n')

# pass 1: split ops and args
for i in range(len(instrs)):
    instrs[i] = instrs[i].split()

# get labels
labels = dict()

for i in range(len(instrs)):
    if instrs[i][0] != 'label':
        continue

    arg = instrs[i][1]

    if arg in labels:
        raise LabelAlreadyFoundException(arg)
    
    labels[arg] = i

if 'main' not in labels:
    raise MainLabelNotFoundException()
else:
    vm.pc = labels['main']

# pass 2: cast args to ints
for i in range(len(instrs)):
    if len(instrs[i]) == 1:
        continue

    op = instrs[i][0]
    arg = instrs[i][1]

    if op == 'push':
        instrs[i][1] = int(arg)
    
    elif op == 'call' or 'j' in op:
        if arg not in labels:
            raise LabelNotFoundException(arg)

        instrs[i][1] = labels[arg]

# call handlers, instruction by instruction
while vm.pc >= 0 and vm.pc < len(instrs):
    instr = instrs[vm.pc]
    op = instr[0]

    if op not in handlers:
        raise InstructionNotFoundException(op)
    
    if len(instr) == 1:
        handlers[op]()
    else:
        arg = instr[1]
        handlers[op](arg)

    vm.pc += 1

raise UnexpectedHaltException()