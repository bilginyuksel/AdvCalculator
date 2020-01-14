
class CalculatorController:
    
    def __init__(self, view, model):
        self._view = view
        self._model = model

        print("Created controller for ",self._view.tab_result,"..")