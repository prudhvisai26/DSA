# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.

# Example 2:
# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

#Approach:
"""
Tortoise-Hare-Approach:
    Intuition: In the Tortoise-Hare approach, we increment slow ptr by 1 and fast ptr by 2, so if take a close look fast ptr will travel double that of the slow pointer. So when the fast ptr will be at the end of the Linked List, slow ptr would have covered half of the Linked List till then. So slow ptr will be pointing towards the middle of Linked List.

Approach: 

Create two pointers slow and fast and initialize them to a head pointer.
Move slow ptr by one step and simultaneously fast ptr by two steps until fast ptr is NULL or next of fast ptr is NULL.
When the above condition is met, we can see that the slow ptr is pointing towards the middle of the Linked List and hence we can return the slow pointer.
"""

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
    
    def middleNode(self):
        slow=self.head
        fast=self.head
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        self.head=slow
    
    def printLL(self):
        temp=self.head
        while(temp):
            print(temp.data,"->",end="")
            temp=temp.next
        print()
ll=Solution()
ll.insertAtBegin(4)
ll.insertAtBegin(3)
ll.insertAtBegin(2)
ll.insertAtBegin(1)

ll.printLL()
ll.middleNode()
ll.printLL()
