from Folder import Folder
from File import File
from MementoReal import MementoReal
from Memento import Memento

C = Folder( "C" )
Winduks=Folder("Видовс")
picture=File("Озеро.жпг")
system32=Folder("сустем32")
Winduks.addContent(system32)
Winduks.addContent(picture)
picture1=File("гора1.жпг")
picture2=File("гора2.жпг")
picture3=File("лужайка.жпг")
system32.addContent(picture1)
system32.addContent(picture2)
Winduks.addContent(picture3)

    