#Remove duplicates from a sorted Doubly Linked List

# Problem statement
# A doubly-linked list is a data structure that consists of sequentially linked nodes, and the nodes have reference to both the previous and the next nodes in the sequence of nodes.

# You are given a sorted doubly linked list of size 'n'.
# Remove all the duplicate nodes present in the linked list.

# Example :
# Input: Linked List: 1 <-> 2 <-> 2 <-> 2 <-> 3
# Output: Modified Linked List: 1 <-> 2 <-> 3
# Explanation: We will delete the duplicate values ‘2’ present in the linked list.

#Code:
class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Don't change the code above.


def removeDuplicates(head: Node) -> Node:
    # Write your code here
    temp=head
    while(temp and temp.next):
        nextNode=temp.next
        while(nextNode and nextNode.data==temp.data):
            nextNode=nextNode.next
        temp.next=nextNode
        if nextNode:
            nextNode.prev=temp
        temp=temp.next
    return head