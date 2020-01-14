
class ComponentFunction:
    
    def __init__(self,fun,val):
        self.fun = fun
        self.expression = val

        # One param functions 
        # example : sin(x), cos(x), abs(x)
        self.type = "basic"

        # Multi param functions
        # example : x^y, modx,y ..
        if type(self.expression) == list: self.type = "advanced"

   
    def __str__(self):
        if self.type =="basic": return "{0}({1})".format(self.fun,self.expression)
    
class ComponentOperator:
    
    def __init__(self,op):
        self.op = op
        #precedence...
    
    def __len__(self):
        return 1

    def __str__(self):
        return self.op

class ComponentValue:

    __pi = (22/7)
    __e = (10) 
    
    def __init__(self,val):
        self.val = val
        self.special_val = [ComponentValue.__pi,ComponentValue.__e]

        self.type = "basic"
        if val in self.special_val: self.type = "special"

    def update(self,val):
        self.val = val

    def __len__(self):
        return len(str(self.val))

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
    
    def __init__(self,ttype = "Scientific"):

        self.open_paranthesis = 0
        self.currentInput = None
        self.display = []
        self.compController = ComponentController()
        self.ttype = ttype


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
        pass

    def cls(self):
        self.currentInput = None
        self.display = ""


# inp = InputController()

# inp.display.append(ComponentFunction("abs","10/32*5"))
# for i in inp.display:
#     print(i)


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