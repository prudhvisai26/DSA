# Reverse a Linked List
# Problem Statement: Problem Statement: Given the head of a singly linked list, write a program to reverse the linked list, and return the head pointer to the reversed list.

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
    
    #Iterative Code:
    def reverse(self):
        temp=self.head
        prev=None
        while temp is not None:
            front=temp.next
            temp.next=prev
            prev=temp
            temp=front
        self.head=prev

    #Recurive Code:
    def reverse_linked_list(self):
        head=self.head
        # Base case:
        # If the linked list is empty or has only one node,
        # return the head as it is already reversed.
        if self.head is None or head.next is None:
            return head
        
        # Recursive step:
        # Reverse the linked list starting from the second node (head.next).
        new_head = self.reverse_linked_list(head.next)
        
        # Save a reference to the node following
        # the current 'head' node.
        front = head.next
        
        # Make the 'front' node point to the current
        # 'head' node in the reversed order.
        front.next = head
        
        # Break the link from the current 'head' node
        # to the 'front' node to avoid cycles.
        head.next = None
        
        # Return the 'new_head,' which is the new
        # head of the reversed linked list.
        self.head=new_head

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

ll.printLL()
ll.reverse()
ll.reverse_linked_list()
ll.printLL()
