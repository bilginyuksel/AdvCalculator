import sys
from PyQt5.QtWidgets import (QStyle,
 QWidget,
 QMainWindow,
QApplication,
QVBoxLayout,
QGridLayout,
QHBoxLayout,
QPushButton,
QLabel,
QLineEdit,
QTabWidget,
QListWidget,
QMenuBar,
QStackedLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import (QIcon,
QColor,
QPalette,
 QFont)
from functools import partial

from body import (ScientificCalculatorBody,
VectorCalculatorBody,
Vector2DCalculatorBody,
ComplexCalculatorBody)

class CalculatorView(QWidget):
    
    def __init__(self, ctype, parent=None, flags=Qt.WindowFlags() ):
        super().__init__(parent=parent, flags=flags)
        self.__set_window_config()
        self.CTYPE = {
            "SCIENTIFIC":ScientificCalculatorBody(),
            "VECTOR 1D":VectorCalculatorBody(),
            "VECTOR 2D":Vector2DCalculatorBody(),
            "COMPLEX":ComplexCalculatorBody()
        }
        
        self.tab_result = ctype
        self.__configuration()

    
    def __configuration(self):
        self.main = QHBoxLayout()
        self.left = QVBoxLayout()
        self.right= QVBoxLayout()
        self.head = QVBoxLayout()
        self.body = self.CTYPE[self.tab_result.upper()]

        self.__set_head()
        self.__set_right()
        self.__set_left()

        self.main.addLayout(self.left)
        self.main.addLayout(self.right)
        self.setLayout(self.main)

    def __set_window_config(self):
        self.setFont(QFont("Times",9))
        
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
        label = QLabel(self.tab_result)
        label.setFont(QFont("default",10))
        self.left.addWidget(label)
        self.left.addLayout(self.head)
        self.left.addLayout(self.body)

    def __update_body(self,body):
        self.body = body


class CalculatorController:
    def __init__(self, view, model):
        self._view = view
        self._model = model
    

class GeneralCalcView(QTabWidget):
    _scientific = "Scientific"
    _complex = "Complex"
    _vector1d = "Vector 1d"
    _vector2d = "Vector 2d"
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setFont(QFont("Times",9))
        self.setWindowOpacity(1)
        self.setWindowIcon(QIcon("assets/calculator.png"))
        self.setWindowTitle("Calculator")
        
        sci = CalculatorView(ctype=GeneralCalcView._scientific)
        comp = CalculatorView(ctype=GeneralCalcView._complex)
        vec1 = CalculatorView(ctype=GeneralCalcView._vector1d)
        vec2 = CalculatorView(ctype=GeneralCalcView._vector2d)

        sci_controller  = CalculatorController(sci, None)
        comp_controller = CalculatorController(comp, None)
        vec1_controller = CalculatorController(vec1, None)
        vec2_controller = CalculatorController(vec2, None)


        self.addTab(sci, QIcon("assets/calculator.png"), GeneralCalcView._scientific)
        self.addTab(vec1, QIcon("assets/vector1d.png"), GeneralCalcView._vector1d)
        self.addTab(vec2, QIcon("assets/vector2d.png"), GeneralCalcView._vector2d)
        self.addTab(comp, QIcon("assets/complex.png"), GeneralCalcView._complex)
   
        



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
    view = GeneralCalcView()
    view.show()
    sys.exit(app.exec_())