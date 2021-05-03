from Folder import Folder
from File import File
from Memento import Memento

class CareTaker():
    def __init__(self):
        self.states=[]
    
    def saveState(self,memento):
        self.states.append(memento)
    
    def restoreMemnto(self,i):
        return self.states[i]