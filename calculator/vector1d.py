from .base import BaseOperator
import numpy as np
class Vector1dOperator(BaseOperator):
    def __init__(self):
        super().__init__()
    def add(self,val1,val2):
        if(len(val1)==len(val2)):
            return np.add(val1,val2)
    def substract(self,val1,val2):
        if(len(val1)==len(val2)):
            return np.subtract(val1,val2)
    def divide(self,val1,val2):
        if not isinstance(val1,list) or not isinstance(val2,list):
            return np.divide(val1,val2)
    def multiply(self,val1,val2):
        if not isinstance(val1,list) or not isinstance(val2,list):
            return np.multiply(val1,val2)
        elif len(val1)==1 or len(val2)==1:
            return np.multiply(val1,val2)
        elif len(val1)==len(val2):
            return np.multiply(val1,val2)