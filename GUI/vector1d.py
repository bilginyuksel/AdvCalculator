class VectorCalculator:

    __instance = None

    @staticmethod
    def getInstance():
        if VectorCalculator.__instance == None:
            VectorCalculator.__instance = VectorCalculator()
        
        return VectorCalculator.__instance

    def __init__(self):
        # virtually private constructor
        if VectorCalculator.__instance != None:
            raise Exception("This class is a singleton !")
        VectorCalculator.__instance = self

    

v = VectorCalculator()
vv = VectorCalculator.getInstance()

print(v)
print(vv)
# v1 = VectorCalculator()
# print(v1)