import numpy as np
class Vector1dOperator():
    def __init__(self):
        pass
    def add(self,vector1,vector2):
        if(len(vector1)==len(vector2)):
            return np.add(vector1,vector2)
        else:
            return "Matrisler Eşit Olmalı..."
    def substract(self,vector1,vector2):
        return np.subtract(vector1,vector2)
    def divide(self,vector1,vector2):
        return vector1/vector2
    def multiply(self,vector1,vector2):
        return vector1*vector2

v1=Vector1dOperator()
print(v1.add([1,2],[2,3,1]))
print(v1.substract([1,2],[2,3]))
