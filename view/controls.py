from functools import partial


class CalculatorController:
    
    def __init__(self, view, model):
        self._view = view
        self._model = model
        self._link_buttons()

        # print("Created controller for ",self._view.tab_result,"..")
        # print("Input controller type ",self._model.ttype)
        

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
        self._view.body.operators['('].clicked.connect(partial(self._op_paranthesis,'('))
        self._view.body.operators[')'].clicked.connect(partial(self._op_paranthesis,')'))
        self._view.body.operators['<-'].clicked.connect(self._op_backspace)
        self._view.body.operators['='].clicked.connect(self._op_equ)


        # @@Basic Functions
        # Bad usage...
        if self._model.ttype == "Scientific":
            for i in self._view.body.basic_functions.keys():
                self._view.body.basic_functions[i].clicked.connect(partial(self._func_basic,i))

    def _num_any(self,obj_name):
        self._model.typeValue(obj_name)
        self._view.updateExpression(self._model.getDisplayValue())
        self._view.updateResult(obj_name)

    def _op_base(self,op):
        self._model.typeOperator(op)
        self._view.updateExpression(self._model.getDisplayValue())

    def _op_paranthesis(self,paranthesis):
        self._model.typeParanthesis(paranthesis)
        self._view.updateExpression(self._model.getDisplayValue())

    def _op_backspace(self):
        self._model.typeBackspace()
        self._view.updateExpression(self._model.getDisplayValue())

    def _op_neg(self):
        # make minus we need to integrate this some other way
        val = self._model.negatiate()
        self._view.updateExpression(self._model.getDisplayValue())
        self._view.updateResult(val)

    def _func_basic(self,func):
        # fill expression 
        self._model.typeFunction(func,None)
        self._view.updateExpression(self._model.getDisplayValue())
        

    def _op_equ(self):
        # Solve the equation with the help of tokenizer
        print(self._model.getDisplayValue())

        
 
