class Link:
    def __init__(self, iData, dData):
        self.iData = iData              # data item (key)
        self.dData = dData             # data item
        self.next = None               # next link in list
    
    def displayLink(self):
        print(f"{{{self.iData}, {self.dData}}}", end=" ")

class LinkList:
    def __init__(self):
        self.first = None              # ref to first link on list
    
    def insertFirst(self, id, dd):
        newLink = Link(id, dd)
        newLink.next = self.first      # points to old first
        self.first = newLink           # now first points to this
    
    def find(self, key):
        current = self.first
        while current is not None:
            if current.iData == key:
                return current
            current = current.next
        return None
    
    def delete(self, key):
        current = self.first
        previous = None
        
        while current is not None:
            if current.iData == key:
                if previous is None:  # deleting first element
                    self.first = current.next
                else:
                    previous.next = current.next
                return current
            previous = current
            current = current.next
        return None
    
    def displayList(self):
        print("List (first-->last): ", end="")
        current = self.first
        while current is not None:
            current.displayLink()
            current = current.next
        print()

#todo o codigo acima foi disponibilizado pelo professor em Java, e foi utilizado IA para convertar para Python


#Lista de Exercícios – Estruturas de Dados Dinâmicas (Java)Utilize as classes anexadas (linkList2.java, linkQueue.java, linkStack.java, doublyLinked.java) para resolver os exercícios abaixo.

