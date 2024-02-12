class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
        self.prev=None
        pass

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head=None

    def insertAtfront(self,data):
        newNode=Node(data)

        newNode.next=self.head
        newNode.prev=None

        if self.head is not None:
            self.head.prev=newNode
        
        self.head=newNode
    
    def insertAtTail(self,data):
        newNode=Node(data)
        current=self.head

        if current is None:
            return current
        while(current.next):
            current=current.next
        
        current.next=newNode
        newNode.prev=current
    
    def deleteLastNode(self):
        current=self.head
        
        if self.head.next is None or self.head is None:
            return None
        while(current.next):
            previous=current
            current=current.next
        previous.next=None
        current.prev=None
    
    def reverseDLL(self):
        current=self.head
        if current is None or current.next is None:
            self.printLL()
            return
        last=None
        while(current):
            last=current.prev
            current.prev=current.next
            current.next=last
            current=current.prev
        self.head=last.prev
        
    def printLL(self):
        temp=self.head
        while(temp):
            print(temp.data,"->",end="")
            temp=temp.next
        print()
    
dl=DoublyLinkedList()

dl.insertAtfront(1)

dl.insertAtTail(2)
dl.insertAtTail(3)
dl.insertAtTail(4)

dl.printLL()
dl.deleteLastNode()
dl.printLL()
dl.reverseDLL()
dl.printLL()

