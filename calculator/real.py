from .base import BaseOperator

class RealOperator(BaseOperator):
    def __init__(self,op):
        super().__init__()
        self.op = op
        self.operations = {
            '+':self.add,
            '-':self.substract,
            '/':self.divide,
            '*':self.multiply
        }
    def add(self,val1,val2):
        return val1+val2
    def substract(self,val1,val2):
        return val1-val2
    def divide(self,val1,val2):
        return val1/val2
    def multiply(self,val1,val2):
        return val1*val2
    def solve(self,val1,val2):
        return self.operations[self.op](val1,val2)
    

