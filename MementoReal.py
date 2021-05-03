from Memento import Memento
class MementoReal(Memento):
    def __init__(self):
        self.state=[]
    def state(self,state):
        self.state=state


        #if len(state.content) != 0:
        #    self.MemCont=state.content
        #    for num in range(len(state.content)):
        #        if state.content[num] is Folder:
        #            self.MemCont.append(state.content[num])
        #            state.content.[num].createMemento()
        #        else:self.MemCont.append(state.content[num])


