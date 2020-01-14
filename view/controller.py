from functools import partial

class CalculatorController:
    
    def __init__(self, view, model):
        self._view = view
        self._model = model

        self.temp = ""

        print("Created controller for ",self._view.tab_result,"..")
        print("Input controller type ",self._model.ttype)

        self._link_buttons()


    def _link_buttons(self):
        # @@Numbers
        for i in self._view.body.numbers.keys():
            self._view.body.numbers[i].clicked.connect(partial(self._num_any,i))

        # @@Operators
        self._view.body.operators['+'].clicked.connect(partial(self._op_base,'+'))
        self._view.body.operators['-'].clicked.connect(partial(self._op_base,'-'))
        self._view.body.operators['/'].clicked.connect(partial(self._op_base,'/'))
        self._view.body.operators['x'].clicked.connect(partial(self._op_base,'x'))
        self._view.body.operators['+/-'].clicked.connect(self._op_neg)
        self._view.body.operators['('].clicked.connect(self._op_pstart)
        self._view.body.operators[')'].clicked.connect(self._op_pend)
        self._view.body.operators['='].clicked.connect(self._op_equ)


        # @@Basic Functions
        # Bad usage...
        if self._model.ttype == "Scientific":
            for i in self._view.body.basic_functions.keys():
                self._view.body.basic_functions[i].clicked.connect(partial(self._func_basic,i))

    def _num_any(self,obj_name):
        self._model.typeValue(obj_name)

    def _op_base(self,op):
        # self._model.typeOperator()
        print(op)
        pass

    def _op_pstart(self):
        # self._model.typeOperator()
        pass

    def _op_pend(self):
        # self._model.typeOperator()
        pass

    def _op_neg(self):
        # self.model.typeValue()
        pass

    def _func_basic(self,func):
        print(func)
        # Wait for expression
        pass

    def _op_equ(self):
        # Solve the equation with the help of tokenizer
        pass
        
 
