
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

    _pi = (22/7)
    _e = (10) 
    
    def __init__(self,val):
        self.val = val
        self.special_val = [ComponentValue._pi,ComponentValue._e]

        self.type = "basic"
        if val in self.special_val: self.type = "special"

    def update(self,val):
        self.val = val

    def __len__(self):
        return len(str(self.val))

    def __str__(self):
        return self.val

class ComponentController:

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


    def typeFunction(self,func):
        self.display.pop() # delete last element which is a value
        # than add the function-- because value goes into function
        self.display.append(self.compController.createFunctionComponent(func,self.currentInput))

    def typeValue(self,val):
        self.display.append(self.compController.createValueComponent(val))

    def typeOperator(self,op):
        self.display.append(self.compController.createOperatorComponent(op))



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


---------------------
[3, +, sin(120)]
[<class ComponentValue>, <class ComponentOperator>, <class ComponentFunction>]
if isinstance(ComponentValue):
    a = comp.value -> ([1,2,3,4],53,[[1,2],[2,3]],5+3i)
    Operator(comp.type).compute(val1,val2) -> 'complex','vector','real'

ComponentFunction('sin','3+5*20') -> basic
    comp.expression = comp.resolve(comp.expression)
    funcManager.solve(comp.func,comp.expression)
ComponentFunction('mod',['5','7']) -> advanced
ComponentFunction('x^y',[5,3]) -> advanced = 125

"""