"""
Problem statement
You must implement the Stack data structure using a Singly Linked List.
Create a class named 'Stack' which supports the following operations(all in O(1) time):

getSize: Returns an integer. Gets the current size of the stack
isEmpty: Returns a boolean. Gets whether the stack is empty
push: Returns nothing. Accepts an integer. Puts that integer at the top of the stack
pop: Returns nothing. Removes the top element of the stack. It does nothing if the stack is empty.
getTop: Returns an integer. Gets the top element of the stack. Returns -1 if the stack is empty

4
3 5
3 4
1
2
Sample Output 1:
2
false    
Explanation for Sample Output 1:
The first two queries ('3') push 5 and 4 on the stack. So the size of the stack becomes 2. 

Therefore the third query ('1') prints the size, and since the stack is not empty, the fourth and final query ('2') outputs "false"
"""
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class Stack:
    # Write your code here
    def __init__(self):
        slef.head=None
        
    def getSize(self):
        # Write your code here
        if self.isEmpty:
            return 0
        else:
            size=0
            temp=self.head
            while(temp):
                size+=1
                temp=temp.next
            return size
        pass

    def isEmpty(self):
        # Write your code here
        if self.head==None:
            return True
        return False
        pass

    def push(self, data):
        # Write your code here
        if self.head==None:
            self.head=Node(data)
        else:
            newNode=Node(data)
            newNode.next=self.head
            self.head=newNode
        pass

    def pop(self):
        # Write your code here
        if self.isEmpty()==False:
            self.head=self.head.next    
        pass
    def getTop(self):
        # Write your code here
        if self.isEmpty():
            return -1
        return self.head.data
        pass
