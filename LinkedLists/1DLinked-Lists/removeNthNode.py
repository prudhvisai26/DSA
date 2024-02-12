# Remove N-th node from the end of a Linked List
# Problem Statement: Given a linked list and an integer N, the task is to delete the Nth node from the end of the linked list and print the updated linked list.


# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]



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
    
    def removeNthFromEnd(self,n):
        slow=self.head
        fast=self.head
        
        for i in range(n):
            fast=fast.next
        if not fast:
            return self.head.next
        while(fast.next):
            slow=slow.next
            fast=fast.next
        
        delete=slow.next
        slow.next=slow.next.next
        delete=None
    
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

ll.removeNthFromEnd(2)

ll.printLL()
