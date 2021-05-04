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

    def delete(self):
        del self.content[0]
        #for i in range(len(self.content)):
        #    if self.content[i].name == name :
        #        del self.content[i]
#
    def getName(self):
        return self.name

    def getContent(self):
        return self.content

    def copy(self):
        copyFolder=Folder(self.name)
        for cont in self.content:
            copyFolder.addContent(cont.copy())
        return copyFolder
        