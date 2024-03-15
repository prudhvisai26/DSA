"""
Problem statement

You are given a circular array 'a' of length 'n'.
A circular array is an array in which we consider the first element is next of the last element. That is, the next element of 'a[n - 1]' is 'a[0]'.
Find the Next Greater Element(NGE) for every element.
The Next Greater Element for an element 'x' is the first element on the right side of 'x' in the array, which is greater than 'x'.
If no greater elements exist to the right of 'x', consider the next greater element as -1.

Example:
Input: 'a' = [1, 5, 3, 4, 2]
Output: NGE = [5, -1, 4, 5, 5]
Explanation: For the given array,
- The next greater element for 1 is 5.
- There is no greater element for 5 on the right side. So we consider NGE as -1.
- The next greater element for 3 is 4.
- The next greater element for 4 is 5, when we consider the next elements as 4 -> 2 -> 1 -> 5.
- The next greater element for 2 is 5, when we consider the next elements as 2 -> 1 -> 5.

"""
from typing import List

def nextGreaterElementII(a: List[int]) -> List[int]:
    # Write your code here.
    n=len(a)
    ans=[-1]*n
    st=[]
    for i in range(2*n-1,-1,-1):
        while st:
            if st[-1]>a[i%n]:
                ans[i%n]=st[-1]
                st.append(a[i%n])
                break
            else:
                st.pop()
        if len(st)==0:
            st.append(a[i%n])
    return ans
    pass
