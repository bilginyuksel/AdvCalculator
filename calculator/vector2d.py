import numpy as np
@staticmethod
def sameSize(vector1,vector2):
        if(len(vector1)==len(vector2)):
            for i in range(len(vector1)):
                if(len(vector1[i])!=len(vector2[i])):
                    return False
        else:
            return False
        return True
class Vector2dOperator:
    def __init__(self):
        pass
    def add(self,vector1,vector2):
        if(sameSize(vector1,vector2)):
            return np.add(vector1,vector2)
        else:
            return "Matrisler aynı boyut olmalı..."
    def substract(self,vector1,vector2):
        if(sameSize(vector1,vector2)):
            return np.subtract(vector1,vector2)
        else:
            return "Matrisler Aynı Boyut Olmalı..."
    def divide(self,vector1,vector2):
        return vector1/vector2
    def multiply(self,vector1,vector2):
        return vector1*vector2
    
v1=Vector2dOperator()
print(v1.add([[4.0, 3.0], [2.0, 1.0]],[[5.0, .0], [2.0, 1.0]]))
print(v1.substract([1,2],[2,3]))
