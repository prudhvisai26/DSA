# Reverse Linked List in groups of Size K
# Problem Statement: Given the head of a singly linked list of `n` nodes and an integer `k`, where k is less than or equal to `n`. Your task is to reverse the order of each group of `k` consecutive nodes, 
# if `n` is not divisible by `k`, then the last group of remaining nodes should remain unchanged.

# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getKthNode(temp,k):
    k-=1
    while temp and k>0:
        k-=1
        temp=temp.next
    return temp
def reverse(head):
    temp=head
    prev=None
    while temp:
        front=temp.next
        temp.next=prev
        prev=temp
        temp=front
    return prev
class Solution:
    def reverseKGroup(self, head,k):
        temp=head
        prevLast=None
        while temp:
            kthNode=getKthNode(temp,k)
            if kthNode is None:
                if prevLast:
                    prevLast.next=temp
                break
            nextNode=kthNode.next
            kthNode.next=None
            
            reverse(temp)
            if temp==head:
                head=kthNode
            else:
                prevLast.next=kthNode
            prevLast=temp
            temp=nextNode
        return head
        