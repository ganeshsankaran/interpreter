class LabelAlreadyFoundException(BaseException):
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return 'Label \'{}\' already found!'.format(self.name)

class MainLabelNotFoundException(BaseException):
    def __str__(self):
        return 'Label \'main\' not found!'

class LabelNotFoundException(BaseException):
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return 'Label \'{}\' not found!'.format(self.name)

class InstructionNotFoundException(BaseException):
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return 'Instruction \'{}\' not found!'.format(self.name)

class UnexpectedHaltException(BaseException):
    def __str__(self):
        return 'Program halted unexpectedly!'

class OperandStackEmptyException(BaseException):
    def __str__(self):
        return 'Operand stack is empty!'

class CallStackEmptyException(BaseException):
    def __str__(self):
        return 'Call stack is empty!'