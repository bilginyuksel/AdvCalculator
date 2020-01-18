import math 

class RealFunctions:
    def __init__(self):
        self.functions = {
            "sin":self.sin,
            "cos":self.cos,
            "tan":self.tan,
            "n!":self.factorial,
            "ln":self.ln,
            "|x|":self.fabs,
            "2^x":self.twoPowerOfX,
        }
    def sin(self,val):
        return math.sin(val)
    def cos(self,val):
        return math.cos(val)
    def tan(self,val):
        return math.tan(val)
    def factorial(self,val):
        return math.factorial(val)
    def ln(self,val):
        return math.log1p(val)
    def fabs(self,val):
        return math.fabs(val)
    def twoPowerOfX(self,val):
        return math.pow(2,val)


