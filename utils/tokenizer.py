from utils.component import ComponentFunction,ComponentOperator,ComponentParanthesis,ComponentValue
from calculator.functions.realfunctions import RealFunctions
from calculator.real import Real
def vector1d(content):
    # Function properties
    return content
def real(content):
    valStack = []
    opStack = []
    for item in content:
        if(isinstance(item,ComponentValue)):
            valStack.append(item.val)
        elif(isinstance(item,ComponentFunction)):
            funcVal = real(item.expression)
            rf = RealFunctions(item.func,funcVal)
            valStack.append(rf.solve)
        elif(isinstance(item,ComponentParanthesis)):
            if(item.__str__ == '('):
                opStack.append(item.__str__)
            else:
                while opStack[-1]!='(':
                    op = opStack.pop()
                    rightVal = valStack.pop()
                    leftVal = valStack.pop()
                    r = Real(op)
                    valStack.append(r.solve(leftVal,rightVal))
                opStack.pop()
        elif(isinstance(item,ComponentOperator)):
            while len(opStack)>0 and ComponentOperator(opStack[-1]).precedence>=item.precedence:
                op = opStack.pop()
                rightVal = valStack.pop()
                leftVal = valStack.pop()
                r = Real(op)
                valStack.append(r.solve(leftVal,rightVal))
            opStack.append(item.__str__)
    while len(opStack)>0:
        op = opStack.pop()
        rightVal = valStack.pop()
        leftVal = valStack.pop()
        r = Real(op)
        valStack.append(r.solve(leftVal,rightVal))
    return valStack.pop()

class Tokenizer:
    
    def __init__(self,tType):

        self.tokenizer_type = tType

        self.tokenizers = {
            "vector1d":vector1d,
            "real":real
        }

    def tokenize(self,content):
        # Maybe do some controls here.
        return self.tokenizers[self.tokenizer_type](content)


vectorTokenizer = Tokenizer("vector1d")
result = vectorTokenizer.tokenize("[1,2] + [3,4]/2")

complexTokenizer = Tokenizer("real")
result = complexTokenizer.tokenize("sin(100)/2 + (5*cos(180))")