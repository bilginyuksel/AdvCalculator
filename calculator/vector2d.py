from .base import BaseOperator
import numpy as np
class Vector2dOperator(BaseOperator):
    def __init__(self):
        pass
    def add(self,val1,val2):
        if len(val1)==len(val2) and len(val1[0])==len(val2[0]):
            return np.add(val1,val2)
    def substract(self,val1,val2):
        if len(val1)==len(val2) and len(val1[0])==len(val2[0]):
            return np.subtract(val1,val2)
    def divide(self,val1,val2):
        if not isinstance(val1,list) or not isinstance(val2,list):
            return np.divide(val1,val2)
    def multiply(self,val1,val2):
        if not isinstance(val1,list) or not isinstance(val2,list):
            return np.multiply(val1,val2)
        elif(len(val1)==len(val2[0]) or len(val2)==len(val1[0])):
            return np.dot(val1,val2)
        