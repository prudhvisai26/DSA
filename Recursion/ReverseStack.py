"""
Problem statement
Reverse a given stack of 'N' integers using recursion. You are required to make changes in the input parameter itself.
Note: You are not allowed to use any extra space other than the internal stack space used due to recursion.

Example:
Input: [1,2,3,4,5] 
Output: [5,4,3,2,1]

Sample Input 1 :
3
2 1 3
Sample Output 1 :
3 1 2
Explanation to Sample Input 1 :
Reverse of a give stack is 3 1 2 where first element becomes last and last becomes first.                   
"""

#Code
from typing import List

def insert(s,ele):
    if len(s)==0:
        s.append(ele)
    else:
        temp=s.pop()
        insert(s,ele)
        s.append(temp)
def reverseStack(s: List[int]) -> None:
    # Write your code here.
    if len(s)==0:
        return
    temp=s.pop()
    reverseStack(s)
    insert(s,temp)
    # return s
    pass
