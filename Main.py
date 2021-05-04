from Folder import Folder
from File import File
from Memento import Memento
from CareTaker import CareTaker

C = Folder("C")
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
C.addContent(Winduks)
Security=CareTaker()
Mem = C.createMemento()
Security.saveState(Mem)

C.viewContent()


#C.delete("Озеро.жпг")
#C.content[0].delete("Гора1.жпг")

