from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QLabel,QPushButton,QHBoxLayout,QLineEdit
from PyQt5.QtCore import Qt
import sys

class BodyLayout:

    def __init__(self):
        super().__init__()
        self._create_numbers()
        self._create_operators()

        self.numbers = {
            '0':self.btn_zero,
            '1':self.btn_one,
            '2':self.btn_two,
            '3':self.btn_three,
            '4':self.btn_four,
            '5':self.btn_five,
            '6':self.btn_six,
            '7':self.btn_seven,
            '8':self.btn_eight,
            '9':self.btn_nine
        }

        self.operators = {
            '+':self.btn_add,
            '-':self.btn_sub,
            'x':self.btn_multip,
            '/':self.btn_divide,
            '(':self.btn_start_paranthesis,
            ')':self.btn_end_paranthesis,
            '+/-':self.btn_negative,
            '.':self.btn_dot,
            '=':self.btn_equal,
            'CE':self.btn_clear,
            '<-':self.btn_backspace
        }

       

    def _create_numbers(self):
        # @Numbers
        self.btn_zero = QPushButton("0")
        self.btn_one = QPushButton("1")
        self.btn_two = QPushButton("2")
        self.btn_three = QPushButton("3")
        self.btn_four = QPushButton("4")
        self.btn_five = QPushButton("5")
        self.btn_six = QPushButton("6")
        self.btn_seven = QPushButton("7")
        self.btn_eight = QPushButton("8")
        self.btn_nine = QPushButton("9")

    def _create_operators(self):
        # @Operators
        self.btn_add = QPushButton('+')
        self.btn_sub = QPushButton('-')
        self.btn_multip = QPushButton('*')
        self.btn_divide = QPushButton('/')
        self.btn_start_paranthesis = QPushButton("(")
        self.btn_end_paranthesis = QPushButton(")")
        self.btn_negative = QPushButton('+/-')
        self.btn_dot = QPushButton(".")
        self.btn_equal = QPushButton("=")
        self.btn_clear = QPushButton('CE')
        self.btn_backspace = QPushButton('<-')

    def _create_buttons(self):
        pass

    def _set_layout(self):
        pass


class VectorCalculatorBody(QVBoxLayout, BodyLayout):
    def __init__(self):
        super().__init__()
        self._create_buttons()


    def _create_buttons(self):
        self.open_dialog = QPushButton(self,"Create Vector")
        self.addWidget()
        return super()._create_buttons()

    def _set_layout(self):
        return super()._set_layout()
    

class Vector2DCalculatorBody(QVBoxLayout, BodyLayout):
    def __init__(self):
        super().__init__()
        self._create_buttons()


    def _create_buttons(self):
        return super()._create_buttons()

    def _set_layout(self):
        return super()._set_layout()

class ComplexCalculatorBody(QVBoxLayout, BodyLayout):
    
    def __init__(self):
        super().__init__()
        self._create_buttons()


    def _create_buttons(self):
        return super()._create_buttons()

    def _set_layout(self):
        return super()._set_layout()
    

class ScientificCalculatorBody(QVBoxLayout, BodyLayout):
    
    def __init__(self):
        super().__init__()
        self._create_buttons()


        self.special_numbers = {
            'pi':self.btn_pi,
            'e':self.btn_e
        }

        self.basic_functions = {
            '1/x':self.btn_onedivx,
            '|x|':self.btn_abs,
            'exp':self.btn_exp,
            'n!':self.btn_fact,
            'ln':self.btn_ln,
            '10^x':self.btn_tentox,
            'x^3':self.btn_cube,
            'x^2':self.btn_square,
            '2^x':self.btn_twotox,
            'sin':self.btn_sin,
            'cos':self.btn_cos,
            'tan':self.btn_tan,
            'cot':self.btn_cot
        }

        self.advanced_functions = {
            'mod':self.btn_mod,
            'log':self.btn_log,
            'x^y':self.btn_xtoy,
            'rand':self.btn_rand
        }

    
        self._set_layout()

    def _create_buttons(self):
        # @Special Numbers
        self.btn_pi = QPushButton("pi")
        self.btn_e = QPushButton('e')

        # @Basic Functions
        self.btn_onedivx = QPushButton("1/x")
        self.btn_abs = QPushButton('|x|')
        self.btn_exp = QPushButton('exp')
        self.btn_fact = QPushButton('n!')
        self.btn_ln = QPushButton('ln')
        self.btn_tentox = QPushButton('10^x')
        self.btn_cube = QPushButton('x^3')
        self.btn_square = QPushButton('x^2')
        self.btn_twotox = QPushButton('2^x')
        self.btn_sin = QPushButton('sin')
        self.btn_cos = QPushButton('cos')
        self.btn_tan = QPushButton('tan')
        self.btn_cot = QPushButton('cot')

        # @Advanced Functions
        self.btn_mod = QPushButton('mod')
        self.btn_log = QPushButton('log')
        self.btn_xtoy = QPushButton('x^y')
        self.btn_rand = QPushButton('rand')
   
    def _set_layout(self):
        
        first_five_buttons = QHBoxLayout()
        first_five_buttons.addWidget(self.basic_functions['sin'])
        first_five_buttons.addWidget(self.basic_functions['cos'])
        first_five_buttons.addWidget(self.basic_functions['tan'])
        first_five_buttons.addWidget(self.basic_functions['cot'])
        first_five_buttons.addWidget(self.advanced_functions['rand'])

        second_five_buttons = QHBoxLayout()
        second_five_buttons.addWidget(self.basic_functions['2^x'])
        second_five_buttons.addWidget(self.special_numbers['pi'])
        second_five_buttons.addWidget(self.special_numbers['e'])
        second_five_buttons.addWidget(self.operators['CE'])
        second_five_buttons.addWidget(self.operators['<-'])

        third_five_buttons = QHBoxLayout()
        third_five_buttons.addWidget(self.basic_functions['x^2'])
        third_five_buttons.addWidget(self.basic_functions['1/x'])
        third_five_buttons.addWidget(self.basic_functions['|x|'])
        third_five_buttons.addWidget(self.basic_functions['exp'])
        third_five_buttons.addWidget(self.advanced_functions['mod'])

        fourth_five_buttons = QHBoxLayout()
        fourth_five_buttons.addWidget(self.basic_functions['x^3'])
        fourth_five_buttons.addWidget(self.operators['('])
        fourth_five_buttons.addWidget(self.operators[')'])
        fourth_five_buttons.addWidget(self.basic_functions['n!'])
        fourth_five_buttons.addWidget(self.operators['/'])

        fifth_five_buttons = QHBoxLayout()
        fifth_five_buttons.addWidget(self.advanced_functions['x^y'])
        fifth_five_buttons.addWidget(self.numbers['7'])
        fifth_five_buttons.addWidget(self.numbers['8'])
        fifth_five_buttons.addWidget(self.numbers['9'])
        fifth_five_buttons.addWidget(self.operators['x'])

        sixth_five_buttons = QHBoxLayout()
        sixth_five_buttons.addWidget(self.basic_functions['10^x'])
        sixth_five_buttons.addWidget(self.numbers['4'])
        sixth_five_buttons.addWidget(self.numbers['5'])
        sixth_five_buttons.addWidget(self.numbers['6'])
        sixth_five_buttons.addWidget(self.operators['-'])

        seventh_five_buttons = QHBoxLayout()
        seventh_five_buttons.addWidget(self.advanced_functions['log'])
        seventh_five_buttons.addWidget(self.numbers['1'])
        seventh_five_buttons.addWidget(self.numbers['2'])
        seventh_five_buttons.addWidget(self.numbers['3'])
        seventh_five_buttons.addWidget(self.operators['+'])

        eighth_five_buttons = QHBoxLayout()
        eighth_five_buttons.addWidget(self.basic_functions['ln'])
        eighth_five_buttons.addWidget(self.operators['+/-'])
        eighth_five_buttons.addWidget(self.numbers['0'])
        eighth_five_buttons.addWidget(self.operators['.'])
        eighth_five_buttons.addWidget(self.operators['='])


        self.addLayout(first_five_buttons)
        self.addLayout(second_five_buttons)
        self.addLayout(third_five_buttons)
        self.addLayout(fourth_five_buttons)
        self.addLayout(fifth_five_buttons)
        self.addLayout(sixth_five_buttons)
        self.addLayout(seventh_five_buttons)
        self.addLayout(eighth_five_buttons)



class Dialog(QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent=parent)


        self.main = QVBoxLayout()
        self.setLayout(self.main)



    def _configuration(self):
        labelrow = QLabel("Row : ")
        labelcol = QLabel("Col : ")
        self.row = QLineEdit()
        self.column = QLineEdit()

        hbox1 = QHBoxLayout()
        hbox.addWidget(labelrow)
        hbox.addWidget(self.row)

        hbox2 = QHBoxLayout()
        hbox.addWidget(labelcol)
        hbox.addWidget(self.column)

        self.main.addLayout(hbox1)
        self.main.addLayout(hbox2)