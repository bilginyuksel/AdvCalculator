import numpy as np
class Vector1dOperator:
    def __init__(self):
        pass
    def add(self,vector1,vector2):
        if(self.sameSize(vector1,vector2)):
            return np.add(vector1,vector2)
        else:
            return "Matrisler aynı boyut olmalı..."
    def substract(self,vector1,vector2):
        if(self.sameSize(vector1,vector2)):
            return np.subtract(vector1,vector2)
        else:
            return "Matrisler Aynı Boyut Olmalı..."
    def divide(self,vector1,vector2):
        return vector1/vector2
    def multiply(self,vector1,vector2):
        return vector1*vector2
    def sameSize(self,vector1,vector2):
        if(len(vector1)==len(vector2)):
            for i in range(len(vector1)):
                if(len(vector1[i])!=len(vector2[i])):
                    return False
        else:
            return False
        return True
v1=Vector1dOperator()
print(v1.add([[4.0, 3.0], [2.0, 1.0]],[[5.0, .0], [2.0, 1.0]]))
print(v1.substract([1,2],[2,3]))
