import math 

class RealFunctions:
    def __init__(self,func,val):
        self.funcs = {
            'sin':math.sin
        }
        self.func = func
        self.val = float(val)
    def solve(self):
        data = self.funcs[self.func](self.val)
        return data

