from PythonBasics.OOP.OOP1 import Calculator2


class childClass(Calculator2):
    num2 = 100

    def __init__(self):
        Calculator2.__init__(self, 2, 10)

    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()