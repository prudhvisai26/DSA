# Odd Even Linked List

# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.
# The first node is considered odd, and the second node is even, and so on.
# Note that the relative order inside both the even and odd groups should remain as it was in the input.

# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]




#Two Pointers Approach:
#Code:
class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
        pass
class Solution:
    def __init__(self):
        self.head=None
    
    def insertAtBegin(self,data):
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            return
        else:
            newNode.next=self.head
            self.head=newNode
            
    def oddEvenList(self):
        head=self.head
        if head is None or head.next is None:
            return head
        odd=head
        even=head.next
        evenHead=head.next
        while(even and even.next):
            odd.next=odd.next.next
            even.next=even.next.next
            odd=odd.next
            even=even.next
        odd.next=evenHead
    
    def printLL(self):
        temp=self.head
        while(temp):
            print(temp.data,"->",end="")
            temp=temp.next
        print()
ll=Solution()
ll.insertAtBegin(5)
ll.insertAtBegin(4)
ll.insertAtBegin(3)
ll.insertAtBegin(2)
ll.insertAtBegin(1)

ll.oddEvenList()

ll.printLL()