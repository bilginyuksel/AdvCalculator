from .base import BaseOperator, OperatorManager

class RealOperator(BaseOperator):
    def __init__(self):
        super().__init__()
        
    def add(self,val1,val2):
        return val1+val2
    def substract(self,val1,val2):
        return val1-val2
    def divide(self,val1,val2):
        return val1/val2
    def multiply(self,val1,val2):
        return val1*val2
   
    

