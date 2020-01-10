import sys
from PyQt5.QtWidgets import (QStyle, QWidget,QMainWindow,
QApplication,QVBoxLayout,QGridLayout,QHBoxLayout,
QPushButton,QLabel,QLineEdit,QTabWidget,QListWidget)
from PyQt5.QtCore import Qt

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
        self.main_layout.addLayout(self.input_layout)
        self.main_layout.addLayout(self.body_layout)
        
        self.memory_layout= QVBoxLayout()
        self.__set_memory_layout()

        self.generalLayout.addLayout(self.main_layout)
        self.generalLayout.addLayout(self.memory_layout)
        self.setLayout(self.generalLayout)

        self.is_functions_open = False

    
    def __set_window_config(self):
        self.setWindowTitle("Calculator")

    def __op_functions(self):
        if self.is_functions_open:
            # Delete all things inside functions
            self.is_functions_open = False
            # self.functions_layout.removeItem(self.functions_layout.itemAt(1))
        # Add trigonometry functions here. 
        # All add all functions here
        # And when you press again, delete all functions.
        else:
            self.functions_layout = QVBoxLayout()
            self.ss = QPushButton("Selam",self)
            self.functions_layout.addWidget(self.ss)
            self.input_layout.addLayout(self.functions_layout)
            self.is_functions_open = True
        

    def __set_input_layout(self):
        self.line_input = QLineEdit("0")
        self.line_input.setReadOnly(True)
        self.line_input.setAlignment(Qt.AlignRight)
        self.input_layout.addWidget(self.line_input)

        # Always update the current operation here.
        h_box = QHBoxLayout()
        self.functions = QPushButton("Trigonometry",self)
        self.functions.clicked.connect(self.__op_functions)
        h_box.addWidget(self.functions)
        self.ghost_compute = QLabel('0')
        self.ghost_compute.setAlignment(Qt.AlignRight)
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
        self.list_memory_formulas = QListWidget()
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
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    view = CalculatorView()
    view.show()
    # controller = CalculatorController(model=model,view=view)
    sys.exit(app.exec_())