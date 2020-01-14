import sys
from PyQt5.QtWidgets import (QStyle, QWidget,QMainWindow,
QApplication,QVBoxLayout,QGridLayout,QHBoxLayout,
QPushButton,QLabel,QLineEdit,QTabWidget,QListWidget,QMenuBar,QStackedLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon,QColor, QPalette, QFont
from functools import partial

from vector1d import ScientificCalculatorBody,VectorCalculatorBody,Vector2DCalculatorBody,ComplexCalculatorBody

class CalculatorView(QWidget):
    
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        self.__set_window_config()
        self.CTYPE = {
            "SCIENTIFIC":ScientificCalculatorBody(),
            "VECTOR1D":VectorCalculatorBody(),
            "VECTOR2D":Vector2DCalculatorBody(),
            "COMPLEX":ComplexCalculatorBody()
        }
        
        self.main = QHBoxLayout()
        self.left = QVBoxLayout()
        self.right= QVBoxLayout()
        self.head = QVBoxLayout()
        self.body = ScientificCalculatorBody()

        self.__set_menu_bar()
        self.__set_head()
        self.__set_right()
        self.__set_left()

        self.main.addLayout(self.left)
        self.main.addLayout(self.right)
        self.setLayout(self.main)

        
        
        print("Numbers\n",self.body.numbers)
        print("Special Numbers\n",self.body.special_numbers)
        print("Operators\n",self.body.operators)
        print("Basic Functions\n",self.body.basic_functions)
        print("Advanced Functions\n",self.body.advanced_functions)

    

    def __set_window_config(self):
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon("assets/calculator.png"))
        self.setWindowOpacity(0.9)
        self.setFont(QFont("Times",9))
        
    def __set_menu_bar(self):
        self.menu = QMenuBar (self)
        calculator = self.menu.addMenu("Calculator")
        scientific = calculator.addAction("Scientific")
        vector_1d = calculator.addAction("1D Vector")
        vector_2d = calculator.addAction("2D Vector")
        complex_num = calculator.addAction("Complex Numbers")

        calculator_help = self.menu.addMenu("Help")
        about = calculator_help.addAction("About")

        scientific.triggered.connect(partial(self.__update_body,self.CTYPE['SCIENTIFIC']))
        vector_1d.triggered.connect(partial(self.__update_body,self.CTYPE['VECTOR1D']))
        vector_2d.triggered.connect(partial(self.__update_body,self.CTYPE['VECTOR2D']))
        complex_num.triggered.connect(partial(self.__update_body,self.CTYPE['COMPLEX']))

    def __set_head(self):
        self.line_input = QLineEdit("0")
        self.line_input.setReadOnly(True)
        self.line_input.setAlignment(Qt.AlignRight)
        self.line_input.setFont(QFont("Consolas",13,QFont.Bold))
        self.head.addWidget(self.line_input)

        # Always update the current operation here.
        h_box = QHBoxLayout()
        # self.functions = QPushButton("Functions",self)
        # self.functions.clicked.connect(self.__op_functions)
        # h_box.addWidget(self.functions)
        self.ghost_compute = QLabel('0')
        self.ghost_compute.setAlignment(Qt.AlignRight)
        self.ghost_compute.setFont(QFont("Consolas",13))
        h_box.addWidget(self.ghost_compute)
        self.head.addLayout(h_box)

    def __set_right(self):
        self.right_tabs = QTabWidget()
        self.list_memory_history = QListWidget()
        self.list_memory_history.addItem("No element on history.")
        self.list_memory_formulas = QListWidget()
        self.list_memory_formulas.addItem("No element on formulas.")

        self.right_tabs.addTab(self.list_memory_history,"History")
        self.right_tabs.addTab(self.list_memory_formulas,"Formulas")
        self.right.addWidget(self.right_tabs)

    def __set_left(self):
        label = QLabel("Scientific Calculator")
        label.setFont(QFont("default",10))
        self.left.addWidget(self.menu)
        self.left.addWidget(label)
        self.left.addLayout(self.head)
        self.left.addLayout(self.body)

    def __update_body(self,body):
        self.body = body
    





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
    sys.exit(app.exec_())