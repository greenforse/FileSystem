from Folder import Folder
from File import File
from MementoReal import MementoReal

class FileSystem(Folder):

    def startRestartState(self,memento):
        self.name = memento.state[0]
        content = memento.state[1]
        self.restartState(content)
