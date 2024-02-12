
# Problem statement
# Given a linked list of 'N' nodes, where each node has an integer value that can be 0, 1, or 2. You need to sort the linked list in non-decreasing order and the return the head of the sorted list.

# Example:
# Given linked list is 1 -> 0 -> 2 -> 1 -> 2. 
# The sorted list for the given linked list will be 0 -> 1 -> 1 -> 2 -> 2.
# Sample Input 1:
# 7
# 1 0 2 1 0 2 1

# Sample Output 1:
# 0 0 1 1 1 2 2

# Sample Input 2:
# 8
# 2 1 0 2 1 0 0 2

# Sample Output 2:
# 0 0 0 1 1 2 2 2



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
    
    def sortList(self):
    # Write your code here
        head=self.head
        zeroHead=Node(-1)
        oneHead=Node(-1)
        twoHead=Node(-1)
    
        zero=zeroHead
        one=oneHead
        two=twoHead
        temp=head
    
        while(temp):
            if(temp.data==0):
                zero.next=temp
                zero=zero.next
            elif(temp.data==1):
                one.next=temp
                one=one.next
            else:
                two.next=temp
                two=two.next
            temp=temp.next
        
        if(oneHead.next):
            zero.next=oneHead.next 
        else: 
            zero.next=twoHead.next
        one.next=twoHead.next
        two.next=None
        self.head=zeroHead.next
    
    def printLL(self):
        temp=self.head
        while(temp):
            print(temp.data,"->",end="")
            temp=temp.next
        print()
ll=Solution()
ll.insertAtBegin(1)
ll.insertAtBegin(0)
ll.insertAtBegin(2)
ll.insertAtBegin(2)
ll.insertAtBegin(0)

ll.sortList()

ll.printLL()
