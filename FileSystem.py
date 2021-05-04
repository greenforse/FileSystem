from Folder import Folder
from File import File
from MementoReal import MementoReal

class FileSystem():
    def __init__(self):
        self.root=Folder("C")

    def createMemento(self):
        return MementoReal(self.root.copy())
        
    def restore(self,memento):
        self.root=memento.state.copy()
