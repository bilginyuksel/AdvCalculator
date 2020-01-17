try:  
    from component import *
    import sys
    sys.path.append("..")
    from calculator.real import RealOperator
    from calculator.functions.realfunctions import RealFunctions
except ImportError as e:
    print(e)

def real(content):
    valStack = []
    opStack = []
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
                    r = RealOperator(op)
                    valStack.append(r.solve(leftVal,rightVal))
                opStack.pop()
        elif(isinstance(item,ComponentOperator)):
            while len(opStack)>0 and ComponentOperator(opStack[-1]).precedence()>=item.precedence():
                op = opStack.pop()
                rightVal = valStack.pop()
                leftVal = valStack.pop()
                r = RealOperator(op)
                valStack.append(r.solve(leftVal,rightVal))
            opStack.append(item.op)
        
    while len(opStack)>0:
        op = opStack.pop()
        rightVal = valStack.pop()
        leftVal = valStack.pop()
        r = RealOperator(op)
        valStack.append(r.solve(leftVal,rightVal))
    return valStack.pop()

class Tokenizer:
    
    def __init__(self,tType):

        self.tokenizer_type = tType

        self.tokenizers = {
            "real":real
        }

    def tokenize(self,content):
        # Maybe do some controls here.
        return self.tokenizers[self.tokenizer_type](content)
