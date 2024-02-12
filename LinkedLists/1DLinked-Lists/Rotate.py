#  Rotate List
# Given the head of a linked list, rotate the list to the right by k places.

# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]



class Solution:
    def rotateRight(self, head,k):
        if head==None or head.next==None or k==0:
            return head
        
        temp=head
        length=1
        while(temp.next):
            length+=1
            temp=temp.next
        temp.next=head
        k=k%length
        end=length-k
        while end:
            temp=temp.next
            end-=1
        head=temp.next
        temp.next=None
        return head