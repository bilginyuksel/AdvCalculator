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
        return self.operators[op](val1,val2)


class BaseOperator:

    def __init__(self):
        # configure operators
        self.name = "Base"


    def add(self,*args):
        raise NotImplementedError

    def substract(self,*args):
        raise NotImplementedError

    def multiply(self,*args):
        raise NotImplementedError

    def divide(self,*args):
        raise NotImplementedError

class RealOperator(BaseOperator):

    def add(self, *args):
        return super().add(*args)

    def substract(self, *args):
        return super().substract(*args)(self):

    def multiply(self, *args):
        return super().multiply(*args)

    def divide(self, *args):
        return super().divide(*args)




realManager = OperatorManager(RealOperator())
realManager.solve(2,3,'+')
# vectorManager = OperatorManager(VectorOperator())

# o_manager = BaseOperatorManager()
# result = o_manager.solve(value_list.pop(),value_list.pop(),op_list.pop())
# f_manager= BaseFunctionManager()
# f_manager.solve(100,'sin')


class Formula:
    def __init__(self,*args):
        super().__init__()
        self.variables, self.operators = tokenize(*args)

    def tokenize(self,*args):
        pass

