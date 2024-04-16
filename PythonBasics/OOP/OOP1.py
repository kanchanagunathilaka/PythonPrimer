class Calculator:
    num = 100 # class variables

    def getData(self):
        print("I'm now executing as method in class")

obj = Calculator()
print(obj.getData())
print(obj.num)
print("*****************************************")

#Constructor is one method which is automatically call when you create object from any other class

class Calculator2:
    num = 100 # class variables
    #Default constructor
    def __init__(self,a, b):
        self.firstMember= a
        self.secondMember= b
        print("I'm the constructor and call automatically")
    def getData(self):
        print("I'm now executing as method in class")

    def Summation(self):
        return self.firstMember + self.secondMember + Calculator2.num


obj2 = Calculator2(2, 3)
print(obj2.getData())
print(obj2.num)
print(obj2.Summation())
print("*****************************************")