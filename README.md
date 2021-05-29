# Interpreter
by Ganesh Sankaran

---

This is a simple interpreter for a simple stack-based ISA.

**Execution**
```
python3 interpreter.py <program name>
```
A sample program is given in `program.txt`.

**ISA**

The ISA is based on [Whitespace's](https://esolangs.org/wiki/Whitespace). My mnemonics can be found in `handlers.py`:
```
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
```

**VM Stack and Heap**

The object `vm` in `handlers.py` contains the program counter, return address stack, operand stack, and runtime heap.
