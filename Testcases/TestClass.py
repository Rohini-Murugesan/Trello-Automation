


class A():
    def __init__(self,b):
        self.a = "10"
        self.b = b

class B(A):
    def __init__(self,b):
        super().__init__(b)

    def printB(self):
        print(self.b)

aobj = A(20)
bobj = B(20)
bobj.printB()