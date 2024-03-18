"""
Problem statement
You are given an array 'arr' of length 'N'.
You are given 'Q' queries, and for each query, you are given an index(0-based indexing).
Answer to each query is the number of the strictly greater elements to the right of the given index element.
You must return an array 'answer' of length ’N’, where ‘answer[i]’ is the answer to the ‘ith’ query.

Example:
Input:
arr = [5, 2, 10, 4], N=4, Q=2, query = [0, 1]
Output:
1 2

Explanation: The element at index 0 is 5 for the first query. There is only one element greater than 5 towards the right, i.e., 10.
For the second query, the element at index 1 is 2. There are two elements greater than 2 towards the right, i.e., 10 and 4. 
Hence we return [1, 2]
"""

from typing import *

def countGreater(N: int, Q: int, arr: List[int], query: List[int]) -> List[int]:
    # Write your code here
    ans=[0]*Q
    for i in range(Q):
        curr=arr[query[i]]
        count=0
        last=N-1
        while(last!=query[i]):
            if arr[last]>curr:
                count+=1
            last-=1
        ans[i]=count
    return ans
    pass
