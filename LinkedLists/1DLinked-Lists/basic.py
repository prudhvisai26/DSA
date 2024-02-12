class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self) -> None:
        self.head=None
    
    def insertAtBegin(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            return
        else:
            newNode.next=self.head
            self.head=newNode

    def insertAtIndex(self,data,index):
        newNode=Node(data)
        pos=0
        current=self.head
        if pos==index:
            self.insertAtBegin(data)
        else:
            while(current and pos+1!=index):
                pos+=1
                current=current.next
            if(current):
                newNode.next=current.next
                current.next=newNode
            else:
                print("Index not found")

    def insertAtEnd(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            return
        current=self.head
        while(current.next):
            current=current.next
        current.next=newNode
    
    def removeFirstNode(self):
        if self.head is None:
            return
        
        self.head=self.head.next

    def deleteNode(self,val):
        current=self.head

        if current.data==val:
            self.removeFirstNode()
            return
        while(current!=None and current.next!=None and current.next.data!=val):
            current=current.next
        
        if current is None or current.next==None:
            print("Data value Not present")
            return
        else:
            current.next=current.next.next
    
    def sizeOfLL(self):
        size=0
        temp=self.head
        while(temp):
            size+=1
            temp=temp.next
        return size
    
    def search(self,value):
        current=self.head
        if current.data==value:
            return True
        while(current):
            if current.data==value:
                return True
            current=current.next
        return False

    def printLL(self):
        temp=self.head
        while(temp):
            print(temp.data,"->",end="")
            temp=temp.next
        print()

l=LinkedList()
l.insertAtBegin(4)
l.insertAtBegin(3)
l.insertAtBegin(2)
l.insertAtBegin(1)

l.insertAtIndex(5,2)
l.insertAtEnd(6)
l.deleteNode(7)
print(l.sizeOfLL())
l.printLL()
print(l.search(50))