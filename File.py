class File():
    def __init__(self,name):
        self.name=name

    def getName(self):
        return self.name

    def rename(self,name):
        self.name=name

    def copy(self):
        copyFile=File(self.name)
        return copyFile
        
    def viewContent(self):
        for i in range (self.tire):
            print("-",end="")
        print(self.name)

    def addTire(self,tire):
        self.tire=tire+1
