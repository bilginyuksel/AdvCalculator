import sys
from PyQt5.QtWidgets import (QStyle, QWidget,QMainWindow,
QApplication,QVBoxLayout,QGridLayout,QHBoxLayout,
QPushButton,QLabel,QLineEdit,QTabWidget,QListWidget,QMenuBar)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon,QColor, QPalette, QFont
from functools import partial
from PyQt5 import QtGui,QtCore
class CalculatorView(QWidget):
    
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)

        self.__set_window_config()

        self.generalLayout = QHBoxLayout()

        self.main_layout = QVBoxLayout()
        self.input_layout = QVBoxLayout()
        self.__set_input_layout()
        self.body_layout = QVBoxLayout()
        self.__set_body_layout()
        label = QLabel("Scientific Calculator")
        label.setFont(QFont("Times",13))
        self.main_layout.addWidget(label)
        self.main_layout.addLayout(self.input_layout)
        self.main_layout.addLayout(self.body_layout)
        
        self.memory_layout= QVBoxLayout()
        self.__set_memory_layout()

        self.generalLayout.addLayout(self.main_layout)
        self.generalLayout.addLayout(self.memory_layout)
        self.setLayout(self.generalLayout)

        # Something is wrong with that
        self.menu = QMenuBar (self)
        self.calculator_type = self.menu.addMenu("Calculator")
        self.calculator_help = self.menu.addMenu("Help")

        
        # self.is_functions_open = False
        self.__op_functions()

    
    def __set_window_config(self):
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon("assets/calculator.png"))
        self.setWindowOpacity(0.8)
        self.setFont(QFont("Times",9))
        

    def __op_functions(self):
        # if self.is_functions_open:
        #     # Delete all things inside functions
        #     # self.is_functions_open = False
        #     pass
        #     # self.functions_layout.removeItem(self.functions_layout.itemAt(1))
        # # Add trigonometry functions here. 
        # # All add all functions here
        # # And when you press again, delete all functions.
        # else:
        #     self.is_functions_open = True
        #     # self.stack = QStackedLayout(self.input_layout)

        h_layout = QHBoxLayout()
        self.pu_sin = QPushButton("sin",self)
        self.pu_cos = QPushButton("cos",self)
        self.pu_tan = QPushButton("tan",self)
        self.pu_cot = QPushButton("cot",self)

        h_layout.addWidget(self.pu_sin)
        h_layout.addWidget(self.pu_cos)
        h_layout.addWidget(self.pu_tan)
        h_layout.addWidget(self.pu_cot)
        h_layout.addStretch()
        self.input_layout.addLayout(h_layout)

        h_layout = QHBoxLayout()
        self.pu_cosec = QPushButton("csc",self)
        self.pu_sec = QPushButton("sec",self)
        self.pu_rand = QPushButton("rand",self)

        h_layout.addWidget(self.pu_cosec)
        h_layout.addWidget(self.pu_sec)
        h_layout.addWidget(self.pu_rand)
        h_layout.addStretch()
        self.input_layout.addLayout(h_layout)

        

    def __set_input_layout(self):
        self.line_input = QLineEdit("0")
        self.line_input.setReadOnly(True)
        self.line_input.setAlignment(Qt.AlignRight)
        self.line_input.setFont(QFont("Consolas",13,QFont.Bold))
        self.input_layout.addWidget(self.line_input)

        # Always update the current operation here.
        h_box = QHBoxLayout()
        # self.functions = QPushButton("Functions",self)
        # self.functions.clicked.connect(self.__op_functions)
        # h_box.addWidget(self.functions)
        self.ghost_compute = QLabel('0')
        self.ghost_compute.setAlignment(Qt.AlignRight)
        self.ghost_compute.setFont(QFont("Consolas",13))
        h_box.addWidget(self.ghost_compute)
        self.input_layout.addLayout(h_box)

    def __set_body_layout(self):
        hbox = QHBoxLayout()
        self.pu_poweroftwo = QPushButton('2^nd',self)
        self.pu_pi = QPushButton('pi',self)
        self.pu_e = QPushButton('e',self)
        self.pu_clear = QPushButton('CE',self)
        self.pu_backspace = QPushButton('<-',self)
        hbox.addWidget(self.pu_poweroftwo)
        hbox.addWidget(self.pu_pi)
        hbox.addWidget(self.pu_e)
        hbox.addWidget(self.pu_clear)
        hbox.addWidget(self.pu_backspace)
        self.body_layout.addLayout(hbox)

        hbox = QHBoxLayout()
        self.pu_xsquare = QPushButton('x^2',self)
        self.pu_onedividex = QPushButton('1/x',self)
        self.pu_abs = QPushButton('|x|',self)
        self.pu_exp = QPushButton('exp',self)
        self.pu_mod = QPushButton('mod',self)
        hbox.addWidget(self.pu_xsquare)
        hbox.addWidget(self.pu_onedividex)
        hbox.addWidget(self.pu_abs)
        hbox.addWidget(self.pu_exp)
        hbox.addWidget(self.pu_mod)
        self.body_layout.addLayout(hbox)

        hbox = QHBoxLayout()
        self.pu_xcube = QPushButton('x^3',self)
        self.pu_paranthesis_start = QPushButton('(',self)
        self.pu_paranthesis_end = QPushButton(')',self)
        self.pu_factorial = QPushButton('n!',self)
        self.pu_divide = QPushButton('/',self)
        hbox.addWidget(self.pu_xcube)
        hbox.addWidget(self.pu_paranthesis_start)
        hbox.addWidget(self.pu_paranthesis_end)
        hbox.addWidget(self.pu_factorial)
        hbox.addWidget(self.pu_divide)
        self.body_layout.addLayout(hbox)

        hbox = QHBoxLayout()
        self.pu_xpower = QPushButton("x^y",self)
        self.pu7 = QPushButton('7',self)
        self.pu8 = QPushButton('8',self)
        self.pu9 = QPushButton('9',self)
        self.pu_multip = QPushButton('x',self)
        hbox.addWidget(self.pu_xpower)
        hbox.addWidget(self.pu7)
        hbox.addWidget(self.pu8)
        hbox.addWidget(self.pu9)
        hbox.addWidget(self.pu_multip)
        self.body_layout.addLayout(hbox)

        hbox = QHBoxLayout()
        self.pu_tentopowerx = QPushButton("10^x",self)
        self.pu4 = QPushButton('4',self)
        self.pu5 = QPushButton('5',self)
        self.pu6 = QPushButton('6',self)
        self.pu_subtract = QPushButton("-",self)
        hbox.addWidget(self.pu_tentopowerx)
        hbox.addWidget(self.pu4)
        hbox.addWidget(self.pu5)
        hbox.addWidget(self.pu6)
        hbox.addWidget(self.pu_subtract)
        self.body_layout.addLayout(hbox)

        hbox = QHBoxLayout()
        self.pu_log = QPushButton('log',self)
        self.pu1 = QPushButton('1',self)
        self.pu2 = QPushButton('2',self)
        self.pu3 = QPushButton('3',self)
        self.pu_add = QPushButton('+',self)
        hbox.addWidget(self.pu_log)
        hbox.addWidget(self.pu1) 
        hbox.addWidget(self.pu2)
        hbox.addWidget(self.pu3)
        hbox.addWidget(self.pu_add)
        self.body_layout.addLayout(hbox)

        hbox = QHBoxLayout()
        self.pu_ln = QPushButton("ln",self)
        self.pu_negative = QPushButton("+/-",self)
        self.pu0 = QPushButton("0",self)
        self.pucomma = QPushButton(",",self)
        self.pu_equal = QPushButton("=",self)
        hbox.addWidget(self.pu_ln)
        hbox.addWidget(self.pu_negative)
        hbox.addWidget(self.pu0)
        hbox.addWidget(self.pucomma)
        hbox.addWidget(self.pu_equal)
        self.body_layout.addLayout(hbox)


    def __set_memory_layout(self):
        self.memory_layout_tabs = QTabWidget()
        self.list_memory_history = QListWidget()
        self.list_memory_history.addItem("No element on history.")
        self.list_memory_formulas = QListWidget()
        self.list_memory_formulas.addItem("No element on formulas.")

        self.memory_layout_tabs.addTab(self.list_memory_history,"History")
        self.memory_layout_tabs.addTab(self.list_memory_formulas,"Formulas")
        self.memory_layout.addWidget(self.memory_layout_tabs)

    def set_display_line_edit(self,content):
        self.line_input.setText(content)

    def set_display_label(self,content):
        self.ghost_compute.setText(content)

    def get_display_line_edit(self):
        return self.line_input.text()

    def add_element_to_history(self,element):
        self.list_memory_history.addItem(element)
    
    def load_formulas(self,formulas):
        self.list_memory_formulas.addItems(formulas)

    def clear_all(self):
        self.line_input.setText("0")
        self.ghost_compute.setText("0")
        
class CalculatorController:

    def __init__(self,model,view):
        self._model = model
        self._view = view
        
        self.token = ""
        self.display = ""
        self.current_number = ""
        self.open_paranthesis = 0
        self.__connect_buttons()

    def __connect_buttons(self):
        self._view.pu0.clicked.connect(partial(self.pb_numbers,self._view.pu0.text()))
        self._view.pu1.clicked.connect(partial(self.pb_numbers,self._view.pu1.text()))
        self._view.pu2.clicked.connect(partial(self.pb_numbers,self._view.pu2.text()))
        self._view.pu3.clicked.connect(partial(self.pb_numbers,self._view.pu3.text()))
        self._view.pu4.clicked.connect(partial(self.pb_numbers,self._view.pu4.text()))
        self._view.pu5.clicked.connect(partial(self.pb_numbers,self._view.pu5.text()))
        self._view.pu6.clicked.connect(partial(self.pb_numbers,self._view.pu6.text()))
        self._view.pu7.clicked.connect(partial(self.pb_numbers,self._view.pu7.text()))
        self._view.pu8.clicked.connect(partial(self.pb_numbers,self._view.pu8.text()))
        self._view.pu9.clicked.connect(partial(self.pb_numbers,self._view.pu9.text()))
    
        self._view.pu_backspace.clicked.connect(self.pb_backspace)
        self._view.pucomma.clicked.connect(self.pb_comma)
        self._view.pu_paranthesis_start.clicked.connect(self.pb_paranthesis_start)
        self._view.pu_paranthesis_end.clicked.connect(self.pb_paranthesis_end)

        self._view.pu_add.clicked.connect(partial(self.pb_operator,"+"))
        self._view.pu_subtract.clicked.connect(partial(self.pb_operator,"-"))
        self._view.pu_divide.clicked.connect(partial(self.pb_operator,"/"))
        self._view.pu_multip.clicked.connect(partial(self.pb_operator,"*"))

        self._view.pu_negative.clicked.connect(self.pb_negative)
        self._view.pu_equal.clicked.connect(self.pb_equal)

        self._view.pu_pi.clicked.connect(partial(self.pb_constants,'pi'))
        self._view.pu_e.clicked.connect(partial(self.pb_constants,'e'))
        self._view.pu_clear.clicked.connect(self.pb_clear)

        self._view.pu_poweroftwo.clicked.connect(partial(self.func_parameter1,'2^x'))
        self._view.pu_xsquare.clicked.connect(partial(self.func_parameter1,'square(x)'))
        self._view.pu_onedividex.clicked.connect(partial(self.func_parameter1,'1/x'))
        self._view.pu_abs.clicked.connect(partial(self.func_parameter1,'abs(x)'))
        self._view.pu_exp.clicked.connect(partial(self.func_parameter1,"exp(x)"))
        self._view.pu_mod.clicked.connect(self.pb_mod)
        self._view.pu_xcube.clicked.connect(partial(self.func_parameter1,'cube(x)'))
        self._view.pu_factorial.clicked.connect(partial(self.func_parameter1,"fact(x)"))
        self._view.pu_xpower.clicked.connect(self.pb_xpower)
        self._view.pu_tentopowerx.clicked.connect(partial(self.func_parameter1,'10^x'))
        self._view.pu_log.clicked.connect(partial(self.func_parameter1,"log"))
        self._view.pu_ln.clicked.connect(partial(self.func_parameter1,"ln(x)"))

        self._view.pu_sin.clicked.connect(partial(self.pb_trigonometry_functions,"sin"))
        self._view.pu_cos.clicked.connect(partial(self.pb_trigonometry_functions,"cos"))
        self._view.pu_tan.clicked.connect(partial(self.pb_trigonometry_functions,"tan"))
        self._view.pu_cot.clicked.connect(partial(self.pb_trigonometry_functions,"cot"))
        self._view.pu_cosec.clicked.connect(partial(self.pb_trigonometry_functions,"cosec"))
        self._view.pu_sec.clicked.connect(partial(self.pb_trigonometry_functions,"sec"))        
        # it is not trigonometric but...
        self._view.pu_rand.clicked.connect(partial(self.pb_trigonometry_functions,"rand"))


    def pb_constants(self,const):
        if len(self.display)>0 and (self.display[-1]==")" or self.__isfloat(self.current_number)):
            pass
        else:
            if const == "pi":   
                self.current_number += str(22/7)
            elif const == 'e':
                self.current_number += str((1+(1/10000))**10000)
                print(self.current_number)

            self.display += const
            self._view.set_display_line_edit(self.display)
            self._view.set_display_label(const)

    def pb_trigonometry_functions(self,func_name):
        pass

    def func_parameter1(self,param1):
        pass


    def pb_log(self):
        pass


    def pb_mod(self):
        pass

    def pb_xpower(self):
        pass

    def pb_operator(self,op):
        if self.current_number != "":
            self.display += op
            self.token += self.current_number + "|"+op+"|"
            self.current_number = ""
            self._view.set_display_line_edit(self.display)

    def pb_negative(self):
        if self.__isfloat(self.current_number):
            n_disp = self.display[:len(self.display)-len(self.current_number)]
            self.current_number = str(float(self.current_number.replace(",","."))*(-1)).replace(".",",")
            n_disp += self.current_number
            self.display = n_disp
            self._view.set_display_line_edit(self.display)   
    def pb_numbers(self,obj):
        # Don't allow paranthesis
        if len(self.display)>0 and (self.display[-1]==")" or self.display[-1]=='e' or self.display[-1]=='i') :
            pass
        else:
            self.display += obj
            self.current_number+=obj
            self._view.set_display_line_edit(self.display)
            self._view.set_display_label(obj)
    def pb_backspace(self):
        if len(self.display)<=1:
            self.display =""
            self.token = ""
            self.current_number=""
            self._view.set_display_line_edit("0")
        else: 
            self.display = self.display[:len(self.display)-1]
            self.current_number = self.current_number[:len(self.current_number)-1]

            if self.token[-1] == '|': self.token = self.token[:len(self.token)-2]
            else: self.token = self.token[:len(self.token)-1]

            print(self.current_number)
            self._view.set_display_line_edit(self.display)
        self._view.set_display_label("0")  
    def pb_comma(self):
        # need to check if i can use comma or not
        if self.current_number.isdigit():
            self.display += ","
            self.current_number += ","
            self._view.set_display_line_edit(self.display)
    def pb_paranthesis_start(self):
        if self.current_number=="":
            self.display += "("
            self.token += "(|"
            self.open_paranthesis+=1
            self._view.set_display_line_edit(self.display)
    def pb_paranthesis_end(self):
        if self.__isfloat(self.current_number) and self.open_paranthesis>0:
            self.open_paranthesis -= 1
            self.display += ")"
            self.token += self.current_number+"|)|"
            self._view.set_display_line_edit(self.display)
            self.current_number = ")"
    def pb_equal(self):
        self.token = (self.token + self.current_number) if self.__isfloat(self.current_number) else self.token[:len(self.token)-1]
        print(self.token)
        print(self.token.split("|"))


    

    def pb_clear(self):
        self.open_paranthesis = 0
        self.display = ""
        self.token = ""
        self.current_number = ""
        self._view.set_display_line_edit("0")
        self._view.set_display_label("0")

    def __isfloat(self,num):
        try:
            float(num.replace(",","."))
            return True
        except ValueError:
            print("Value error")
            return False






if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    app.setPalette(palette)
    view = CalculatorView()
    view.show()
    model = None
    controller = CalculatorController(model=model,view=view)
    sys.exit(app.exec_())