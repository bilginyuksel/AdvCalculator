import numpy as np
from collections import Counter
class Vector1dFunctions:
    def __init__(self):
        self.functions = {
            "median":self.median,
            "mod":self.mod,
            "max":self.maxOfMatrix,
            "min":self.minOfMatrix,
            "sum":self.sumOfElements,
        }
    def median(self,val):
        return np.median(val)
    def mod(self,val):
        bincount = np.bincount(val)
        return np.argmax(bincount)
    def maxOfMatrix(self,val):
        return np.amax(val)
    def minOfMatrix(self,val):
        return np.amin(val)
    def sumOfElements(self,val):
        return np.sum(val)

class Vector2dFunctions:
    def __init__(self):
        self.functions = {
            "mean":self.mean,
            "std":self.std,
            "median":self.median,
            "max":self.maxOfMatrix,
            "min":self.minOfMatrix,
            "sum":self.sumOfElements,
            "inv":self.inv,
            "T":self.transpoz,
            "det":self.determinant
        }
    def mean(self,val):
        return np.mean(val)
    def std(self,val):
        return np.std(val)
    def median(self,val):
        return np.median(val)
    def maxOfMatrix(self,val):
        return np.amax(val)
    def minOfMatrix(self,val):
        return np.amin(val)
    def sumOfElements(self,val):
        return np.sum(val)
    def inv(self,val):
        return np.linalg.inv(val)
    def transpoz(self,val):
        return np.transpose(val)
    def determinant(self,val):
        return np.linalg.det((val))