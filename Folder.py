from MementoReal import MementoReal
from File import File
class Folder():
    def __init__(self,name):
        self.name=name
        self.content=[]
        self.tire=0
    def addContent(self,add):
        self.content.append(add)
        self.content[len(self.content)-1].addTire(self.tire)
    def addTire(self,tire):
        self.tire=tire+1

    def viewContent(self):
        for i in range (self.tire):
            print("-",end="")
        print(f"{self.name}:")
        for content in self.content:
            content.viewContent()

    def delete(self,name):
        for i in range(len(self.content)):
            if self.content[i]==name:
                del self.content[i]

    def getName(self):
        return self.name

    def getContent(self):
        return self.content

    def createMemento(self):
        fileMemento = MementoReal(self.copy)
        #fileMemento.state(self.copy)
        return fileMemento

    def copy(self):
        copyFolder=[]
        copyName=self.name
        copyCont=[]
        if len(self.content) != 0:
            for num in range(len(self.content)):
                copyCont.append(self.content[num])
                copyCont[num].copy()
        copyFolder.append(copyName)
        copyFolder.append(copyCont)
        return copyFolder

    def startRestartState(self,memento):
        self.name = memento.state[0]
        content = memento.state[1]
        self.restartState(content)


    def restartState(self,content):
        reFolder=Folder(content[0])
        del content[0]
        for cont in content:
            if type(cont) == list:
                reFolder.restartState(cont)
                self.addContent(reFolder)
            else:
                filee = File(cont)
                self.addContent(filee)
                
        