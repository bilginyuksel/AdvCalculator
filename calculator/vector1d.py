from .base import BaseOperator
import numpy
class Vector1dOperator(BaseOperator):
    def __init__(self):
        super().__init__()
    def add(self,vector1,vector2):
        return numpy.add(vector1,vector2)
    def substract(self,vector1,vector2):
        return vector1-vector2
    def divide(self,vector1,vector2):
        return vector1/vector2
    def multiply(self,vector1,vector2):
        return vector1*vector2

