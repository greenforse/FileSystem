class File():
    def __init__(self,name):
        self.name=name

    def getName(self):
        return self.name

    def rename(self,name):
        self.name=name

    def copy(self):
        pass

    def restartState(self):
        pass
    def viewContent(self):
        for i in range (self.tire):
            print("-",end="")
        print(self.name)

    def addTire(self,tire):
        self.tire=tire+1
