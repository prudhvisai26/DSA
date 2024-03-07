"""
Problem statement
You are given a stack ‘S’. Your task is to sort the sack recursively.



Note:
Looping through the stack is not allowed.
You need to return a stack that is sorted in descending order.


For example:
Given stack S = 1 3 2 
The output will be 3 2 1 since it is the sorted order.

Sample Input 1 :
2
4
1 0 0 2 
3 
2 4 2
Sample Output 1 :
2 1 0 0
4 4 2
Explanation of the Sample Input 1:
For the first test case:
For the given stack, the resultant sorted stack would be 0 0 1 2.  

For the second test case:
For the given stack, the resulting sorted stack would be 2 2 4.   
"""

def insert(s,ele):
    if len(s)==0 or ele>s[-1]:
        s.append(ele)
        return
    else:
        temp=s.pop()
        insert(s,ele)
        s.append(temp)
def sortStack(s):
    # Write your code here.
    if len(s)==0:
        return s
    temp=s.pop()
    sortStack(s)
    insert(s,temp)
    return s
    pass
