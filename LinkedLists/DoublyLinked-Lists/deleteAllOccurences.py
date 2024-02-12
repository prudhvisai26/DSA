# Delete all occurrences of a given key in a doubly linked list

# Problem statement
# A doubly-linked list is a data structure that consists of sequentially linked nodes, and the nodes have reference to both the previous and the next nodes in the sequence of nodes.

# You’re given a doubly-linked list and a key 'k'.
# Delete all the nodes having data equal to ‘k’.

# Example:
# Input: Linked List: 10 <-> 4 <-> 10 <-> 3 <-> 5 <-> 20 <-> 10 and ‘k’ = 10
# Output: Modified Linked List: 4 <-> 3 <-> 5 <-> 20
# Explanation: All the nodes having ‘data’ = 10 are removed from the linked list.

# Sample Input 1:
# 7
# 10 4 10 3 5 20 10
# 10

# Sample Output 1:
# 4 3 5 20

# Explanation Of Sample Input 1:
# All the nodes having ‘data’ = 10 are removed from the linked list.

class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


def deleteAllOccurrences(head: Node, k: int) -> Node:
    temp=head
    while(temp):
        if temp.data==k:
            if temp==head:
                head=temp.next
            nextNode=temp.next
            prevNode=temp.prev
            if nextNode:
                nextNode.prev=prevNode
            if prevNode:
                prevNode.next=nextNode
            temp=nextNode
        else:
            temp=temp.next
    return head
    pass

