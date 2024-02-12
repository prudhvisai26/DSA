# Find pairs with given sum in doubly linked list

# Problem statement
# A doubly-linked list is a data structure that consists of sequentially linked nodes, and the nodes have reference to both the previous and the next nodes in the sequence of nodes.
# You are given a sorted doubly linked list of size 'n', consisting of distinct positive integers, and a number 'k'.

# Find out all the pairs in the doubly linked list with sum equal to 'k'.

# Example :
# Input: Linked List: 1 <-> 2 <-> 3 <-> 4 <-> 9 and 'k' = 5
# Output: (1, 4) and (2, 3)
# Explanation: There are 2 pairs in the linked list having sum 'k' = 5.


class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

def findTail(head):
    tail=head
    while(tail.next):
        tail=tail.next
    return tail

def findPairs(head: Node, k: int):
    ans=[]
    if head is None or head.next is None:
        return None
    left=head
    right=findTail(head)
    while(left.data< right.data):
        if left.data+right.data==k:
            ans.append((left.data,right.data))
            left=left.next
            right=right.prev
        elif left.data+right.data<k:
            left=left.next
        else:
            right=right.prev
    return ans