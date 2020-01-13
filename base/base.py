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

# Basic Operators 
class BaseOperator:
    
    @staticmethod
    def add(self,val1,val2):
        return val1+val2

    @staticmethod
    def multiply(self,val1,val2):
        return val1*val2

    @staticmethod
    def substract(self,val1,val2):
        return val1-val2

    @staticmethod
    def divide(self,val1,val2):
        return val1/val2


class BaseFunctionManager:
    
    def __init__(self):
        super().__init__()

        self.functions = {

        }

    def solve(self, val, func):
        return self.functions[func](val)


class BaseOperatorManager:
    
    def __init__(self):
        super().__init__()

        self.operators = {
            # how to fill those operators
            '+':BaseOperator.add,
            '-':BaseOperator.substract,
            '*':BaseOperator.multiply,
            '/':BaseOperator.divide
        }

    def solve(self, val1, val2, op):
        return self.operators[op](val1,val2)



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


"""
i think it should be like this
"""
class RealNumber(NumberFormat):

    def __check(self):
        pass
    
    def check_format(self,val):
        assert self.__check(val),"Value is not a real number."

class RealNumberOperator(BaseOperator):
    
    def add(self):
        pass

    def sub(self):
        pass

class RealNumberFunction(BaseFunctionManager):
    
    def abs(self):
        pass
    def square(self):
        pass

class RealNumberManager(RealNumber):

    def __init__(self, nu_value, nu_type='R+'):
        super().__init__(nu_value, nu_type=nu_type)

        operators = RealNumberOperator()
        # It could be special functions, taking arguments bigger than len(1)
        functions = RealNumberFunction("sad")

        self.operator_dict = {
            '+':operators.add,
            '-':operators.sub
        }

        self.function_dict = {
            'abs':functions.abs,
            'square':functions.square
        }


    def make_operation(self,val1,val2,op):
        self.check_format(val1)
        self.check_format(val2)
        return self.operator_dict[op](val1,val2)

    def solve_function(self,*val,func):
        for i in val : self.check_format(i) 
        return self.function_dict[func](*val)


rm = RealNumberManager(3)