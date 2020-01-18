from .component import *
import sys
sys.path.append("..")
from calculator.real import OperatorManager,RealOperator
from calculator.functions.realfunctions import RealFunctions


def real(content,solver = RealOperator()):
    valStack = []
    opStack = []

    op_manager = OperatorManager(solver)
    
    for item in content:
        if(isinstance(item,ComponentValue)):
            valStack.append(item.val)
        elif(isinstance(item,ComponentFunction)):
            funcVal = real(item.expression)
            rf = RealFunctions(item.fun,funcVal)
            valStack.append(rf.solve())
        elif(isinstance(item,ComponentParanthesis)):
            if(item.paranthesis== ComponentParanthesis._start):
                opStack.append(item.paranthesis)
            else:
                while opStack[-1]!=ComponentParanthesis._start:
                    op = opStack.pop()
                    rightVal = valStack.pop()
                    leftVal = valStack.pop()
                    valStack.append(op_manager.solve(leftVal,rightVal,op))
                opStack.pop()
        elif(isinstance(item,ComponentOperator)):
            while len(opStack)>0 and ComponentOperator(opStack[-1]).precedence()>=item.precedence():
                op = opStack.pop()
                rightVal = valStack.pop()
                leftVal = valStack.pop()
                valStack.append(op_manager.solve(leftVal,rightVal,op))
            opStack.append(item.op)
        
    while len(opStack)>0:
        op = opStack.pop()
        rightVal = valStack.pop()
        leftVal = valStack.pop()
        valStack.append(op_manager.solve(leftVal,rightVal,op))
    return valStack.pop()

class Tokenizer:
    
    def __init__(self,tType):

        self.tokenizer_type = tType

        self.solvers = {
            "real":RealOperator()
        }

    def tokenize(self,content):
        # Maybe do some controls here.
        solver = self.solvers[self.tokenizer_type]
        func = self.tokenizers[self.tokenizer_type]
        return func(content,solver)
