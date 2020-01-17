# InputType or another things
# This class is abstract class for all Inputs
# I mean vector, 2DVector, Complexnumber, Number
class InputType:
    
    def __init__(self,type):
        self.type = type

    def __isVector(self):
        return False

    def __is2dVector(self):
        return False

    def __isComplex(self):
        return False

    def __isReal(self):
        return False

    def inputType(self):
        if self.__isVector():
            return "vector"
        elif self.__is2dVector():
            return "2dVector"
        elif self.__isComplex():
            return "complex"
        else: return "real"

"""
According to that input type
run the tokenizer which can tokenize this input type
"""



class FunctionManager:
    
    def __init__(self):

        self.functions = {

        }

    def solve(self, val, func):
        return self.functions[func](val)


class OperatorManager:
    
    def __init__(self,opSolver):

        self.operators = {
            # how to fill those operators
            '+':opSolver.add,
            '-':opSolver.substract,
            '*':opSolver.multiply,
            '/':opSolver.divide
        }

    def solve(self, val1, val2, op):
        assert (not op in self.operators.keys()), "You can't solve anything with paranthesis !"
        return self.operators[op](val1,val2)


class BaseOperator:

    def __init__(self):
        # configure operators
        self.name = "Operator"


    def add(self,*args):
        raise NotImplementedError

    def substract(self,*args):
        raise NotImplementedError

    def multiply(self,*args):
        raise NotImplementedError

    def divide(self,*args):
        raise NotImplementedError




class Formula:
    def __init__(self,*args):
        super().__init__()
        self.variables, self.operators = tokenize(*args)

    def tokenize(self,*args):
        pass

