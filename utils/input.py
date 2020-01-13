
class ComponentFunction:
    
    def __init__(self,fun,val):
        self.fun = fun
        self.val = val
   
    def __str__(self):
        return "{0}({1})".format(self.fun,self.val)
    
class ComponentOperator:
    
    def __init__(self,op):
        super().__init__()
        self.op = op
    def __str__(self):
        return self.op

class ComponentValue:
    
    def __init__(self,val):
        super().__init__()

        self.val = val

    def __str__(self):
        return self.val

class ComponentController:

    def __init__(self):
        super().__init__()

    def createFunctionComponent(self,fun,val):
        return ComponentFunction(fun,val)

    def createOperatorComponent(self,op):
        return ComponentOperator(op)

    def createValueComponent(self,val):
        return ComponentValue(val)
    

class InputController:
    
    def __init__(self):
        super().__init__()

        self.currentInput = None
        self.display = []
        self.compController = ComponentController()


    def addFunction(self,func):
        self.display.pop() # delete last element which is a value
        # than add the function-- because value goes into function
        self.display.append(self.compController.createFunctionComponent(func,self.currentInput))

    def isNumber(self):
        pass

    def isOperator(self):
        pass

    def isFunction(self):
        pass

    def isSpecialNumber(self):
        pass

    def delete(self):
        """
        If you are deleting a number wwith backspace
        321 -> it doesnt matter 32->3 -- you can delete like this
        but if you are deleting a function, that means you have to delete all
        """
        if self.currentInput == self.isFunction():
            self.display.pop()

        elif type(self.currentInput) == float:
            currNumber = self.display[-1]
            # delete one element from currNumber
            if len(currNumber)>0:
                currNumber=currNumber[:len(currNumber)-1]
            
            self.display.pop()
            if len(currNumber)>0: self.display.append(self.compController.createValueComponent(currNumber))

    def cls(self):
        self.currentInput = None
        self.display = ""


inp = InputController()

inp.display.append(Func(3))
for i in inp.display:
    print(i)


"""
'3' '+' 'sin(5)' '/' '10'
Run Parser ----
co = '3', '+', 'sin-5', '/', '10'

ifFunction...
content.split('-')
list[0] -> sin
list[1] -> math process.

tokenize = Tokenizer('real')
result = tokenize.tokenize(co)

result.


isFunction() ->  True
content = sin(5)
solve content RegExp -> ....
--- Function type 2 parameter -> (x^y)s


priority---
value - operator
if function....
do different kind of process.
return Value.. add value stack.



postfix
--- when stack pop's operator
do the process.
val1, val2, process.

"""