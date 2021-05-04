from Folder import Folder
from File import File
from Memento import Memento
from CareTaker import CareTaker
from FileSystem import FileSystem
C = FileSystem()
Winduks=Folder("Видовс")
picture=File("Озеро.жпг")
system32=Folder("сустем32")
Winduks.addContent(system32) #0
Winduks.addContent(picture)#1
picture1=File("гора1.жпг")
picture2=File("гора2.жпг")
picture3=File("лужайка.жпг")
system32.addContent(picture1)#0
system32.addContent(picture2)#1
Winduks.addContent(picture3)#2
C.root.addContent(Winduks)

Security=CareTaker()

C.root.viewContent()

Security.saveState(C.createMemento())

C.root.delete()
C.root.viewContent()
C.restore(Security.restoreMemento(0))

C.root.viewContent()