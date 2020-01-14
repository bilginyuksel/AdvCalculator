from functools import partial

class CalculatorController:
    
    def __init__(self, view, model):
        self._view = view
        self._model = model

        self.temp = ""

        print("Created controller for ",self._view.tab_result,"..")
        print("Input controller type ",self._model.ttype)

        self.link_numbers()

    def link_numbers(self):
        for i in self._view.body.numbers.keys():
            self._view.body.numbers[i].clicked.connect(partial(self.number_click,i))

    def number_click(self,obj_name):
        self.temp += obj_name
        print(self.temp)

        