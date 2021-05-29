from errors import *

# machine state
class VM:
    def __init__(self):
        self.pc = 0
        self.stack = list()
        self.heap = dict()
        self.ras = list()

vm = VM()

def push(arg):
    global vm

    vm.stack.append(arg)

def pop():
    global vm

    if not vm.stack:
        raiseOperandStackEmptyException()
    
    vm.stack.pop()

def dup():
    global vm

    if not vm.stack:
        raiseOperandStackEmptyException()
    
    vm.stack.append(vm.stack[-1])

def swap():
    global vm

    if len(vm.stack) < 2:
        raiseOperandStackEmptyException()
    
    vm.stack[-1], vm.stack[-2] = vm.stack[-2], vm.stack[-1]

def add():
    global vm

    if len(vm.stack) < 2:
        raiseOperandStackEmptyException()
    
    arg = vm.stack[-2] + vm.stack[-1]
    vm.stack = vm.stack[:-2]
    vm.stack.append(arg)

def sub():
    global vm

    if len(vm.stack) < 2:
        raiseOperandStackEmptyException()
    
    arg = vm.stack[-2] - vm.stack[-1]
    vm.stack = vm.stack[:-2]
    vm.stack.append(arg)

def mul():
    global vm

    if len(vm.stack) < 2:
        raiseOperandStackEmptyException() 
    
    arg = vm.stack[-2] * vm.stack[-1]
    vm.stack = vm.stack[:-2]
    vm.stack.append(arg)

def div():
    global vm

    if len(vm.stack) < 2:
        raiseOperandStackEmptyException()
    
    arg = vm.stack[-2] // vm.stack[-1]
    vm.stack = vm.stack[:-2]
    vm.stack.append(arg)

def mod():
    global vm

    if len(vm.stack) < 2:
        raiseOperandStackEmptyException()
    
    arg = vm.stack[-2] % vm.stack[-1]
    vm.stack = vm.stack[:-2]
    vm.stack.append(arg)

def load():
    global vm

    if not vm.stack:
        raiseOperandStackEmptyException()
    
    vm.stack.append(vm.heap[vm.stack.pop()])

def store():
    global vm

    if len(vm.stack) < 2:
        raiseOperandStackEmptyException()

    vm.heap[vm.stack[-2]] = vm.stack[-1]
    vm.stack = vm.stack[:-2]

def label(arg):
    pass

def call(arg):
    global vm

    vm.ras.append(vm.pc)
    vm.pc = arg - 1

def jump(arg):   
    global vm

    vm.pc = arg - 1

def jnil(arg):
    global vm

    if not vm.stack:
        raiseOperandStackEmptyException()
    
    if vm.stack.pop() == 0:
        vm.pc = arg - 1

def jneg(arg):
    global vm

    if not vm.stack:
        raiseOperandStackEmptyException()
    
    if vm.stack.pop() < 0:
        vm.pc = arg - 1

def ret():
    global vm

    if not vm.ras:
        raise CallStackEmptyException()
    
    vm.pc = vm.ras.pop()

def halt():
    print()
    exit(0)

def getchar(arg = None):
    global vm

    vm.stack.append(ord(input()[1]))

def getint(arg = None):
    global vm

    vm.stack.append(int(input()))

def putchar(arg = None):
    global vm

    if not vm.stack:
        raiseOperandStackEmptyException()

    print(chr(vm.stack.pop()), end = '')

def putint(arg = None):
    global vm

    if not vm.stack:
        raiseOperandStackEmptyException()

    print(vm.stack.pop(), end = '')

handlers = {
    'push': push,
    'pop': pop,
    'dup': dup,
    'swap': swap,
    'add': add,
    'sub': sub,
    'mul': mul,
    'div': div,
    'mod': mod,
    'load': load,
    'store': store,
    'label': label,
    'call': call,
    'jump': jump, # unconditional jump
    'jnil': jnil, # jump if TOS == 0
    'jneg': jneg, # jump if TOS < 0
    'ret': ret,
    'halt': halt,
    'getchar': getchar,
    'getint': getint,
    'putchar': putchar,
    'putint': putint
}