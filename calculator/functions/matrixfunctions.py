import numpy 

class Vector1dFunctions:
    def __init__(self):
        self.functions = {
            "median":self.median
        }
    def median(self,val):
        return numpy.median(val)



