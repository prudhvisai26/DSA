# #Add one to a number represented as Linked List

# Problem statement
# You're given a positive integer represented in the form of a singly linked-list of digits. The length of the number is 'n'.
# Add 1 to the number, i.e., increment the given number by one.
# The digits are stored such that the most significant digit is at the head of the linked list and the least significant digit is at the tail of the linked list.

# Example:
# Input: Initial Linked List: 1 -> 5 -> 2
# Output: Modified Linked List: 1 -> 5 -> 3

# Explanation: Initially the number is 152. After incrementing it by 1, the number becomes 153.

# Sample Input 1:
# 3
# 1 5 2
# Sample Output 1:
# 1 5 3

# Sample Input 2:
# 2
# 9 9
# Sample Output 2:
# 1 0 0
# Explanation For Sample Input 2:
# Initially the number is 9. After incrementing it by 1, the number becomes 100. Please note that there were 2 nodes in the initial linked list, but there are three nodes in the sum linked list.

class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def addHelper(temp):
    if temp==None:
        return 1
    carry=addHelper(temp.next)
    temp.data+=carry
    if temp.data<10:
        return 0
    temp.data=0
    return 1


def addOne(head: Node) -> Node:
    # write your code here
    carry=addHelper(head)
    if carry==1:
        newNode=Node(1)
        newNode.next=head
        head=newNode
    return head
