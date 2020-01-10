# InputType or another things
# This class is abstract class for all Inputs
# I mean vector, 2DVector, Complexnumber, Number
class InputMethod:
    pass


# Basic Operators 
class BaseOperator:
    
    def add(self):
        print("Add...")

    def multiply(self):
        pass

    def substract(self):
        pass

    def divide(self):
        pass

class BaseFunctionManager:
    """
    still trying to think,
    should i think trigonometric, logaritmic functions different from real operators (+,-,/,*)
    For matrix operations, inversion,Transpoze. These are not operators.
    """
    def __init__(self,val):
        self.val = val

        

op = BaseOperator()
sample_dict = {
    'o/add/':op.add,
    'o/subtract/':op.substract,
    'o/multiply/':op.multiply,
    'o\\divide\\':op.divide
}

# Example function calling.
sample_dict['o/add/']()

# Normal user input, 
# we will do ghost computing but
# the main process happening when the user push enter button
# This is the one of the most important classes
# Because when user push a button this class will do the job
class InputController:

    __instance = None
    
    def __new__(self):
        return self

    def __init__(self):
        super().__init__()

    def equal(self):
        pass

    def tokenize(self):
        pass

    def ghost_compute(self):
        pass

    def compute(self):
        pass



# Number formats are important
# Because of the output to the real world
# and also the calculations changing with type of output
# The number formats generally :
# RealNumber, ComplexNumber, Vector, 2DVector, Radyal(pi), Logarithmic
class NumberFormat:

    def __init__(self,nu_value,nu_type = 'R+'):
        self.nu_value = nu_value
        self.nu_type = nu_type

        if self.nu_type:
            self.operator = BaseOperator()
    
    def declare_Operator(self):
        raise TypeError

    def is_complex(self):
        return False
    def is_real(self):
        return False
    def is_vector(self):
        return False
    def is_2dVector(self):
        return False
    



class Formula:
    def __init__(self,*args):
        super().__init__()
        self.variables, self.operators = tokenize(*args)

    def tokenize(self,*args):
        pass





# i = Input()
# print(i)
# i1  = Input()
# print(i1)