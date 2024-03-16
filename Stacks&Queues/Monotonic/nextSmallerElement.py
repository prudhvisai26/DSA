"""
Problem statement
You are given an integer array 'a' of size 'n'.
For each element in the array, check whether the immediate right element of the array is smaller or not.
If the next element is smaller, update the current index to that element. If not, then -1. The last element does not have any elements on its right.

Example :
Input: 'a' = [4, 7, 8, 2, 3, 1]
Output: Modified array 'a' = [-1, -1, 2, -1, 1, -1]

Explanation: In the array 'a':
4 has 7 on its right. Since 7 is not smaller, we update 4 to -1.
7 has 8 on its right. Since 8 is not smaller, we update 7 to -1.
8 has 2 on its right. Since 2 is smaller than 8, we update 8 to 2.
2 has 3 on its right. Since 3 is not smaller, we update 2 to -1.
3 has 1 on its right. Since 1 is smaller than 3, we update 3 to 1.
1 does not have any element on right. So we update 1 to -1.
"""

from typing import List

def immediateSmaller(a: List[int]) -> None:
    # Write your code here
    for i in range(len(a)-1):
        if a[i+1]<a[i]:
            a[i]=a[i+1]
        else:
            a[i]=-1
    a[-1]=-1
    pass
