"""
Problem statement
You are given an array 'nums' of ‘n’ integers.
Return all subset sums of 'nums' in a non-decreasing order.

Note:
Here subset sum means sum of all elements of a subset of 'nums'. A subset of 'nums' is an array formed by removing some (possibly zero or all) elements of 'nums'.

For example
Input: 'nums' = [1,2]
Output: 0 1 2 3
Explanation:
Following are the subset sums:
0 (by considering empty subset)
1 
2
1+2 = 3
So, subset sum are [0,1,2,3].

Sample Input 1 :
3
1 2 3
Sample output 1 :
0 1 2 3 3 4 5 6
Explanation For Sample Output 1:
For the first test case,
Following are the subset sums:
0 (by considering empty subset)
1
2
1+2 = 3
3
1+3 = 4
2+3 = 5
1+2+3 = 6
So, subset-sums are [0,1,2,3,3,4,5,6]
"""

from sys import *
from collections import *
from math import *

from typing import List

def findSum(num,n,i,sum,res):
    if i==n:
        res.append(sum)
        return
    
    #PICK the number
    findSum(num,n,i+1,sum+num[i],res)

    #Dont Pick the number
    findSum(num,n,i+1,sum,res)

def subsetSum(num: List[int]) -> List[int]:
    # Write your code here.
    res=[]
    n=len(num)
    findSum(num,n,0,0,res)
    res.sort()
    return res
    pass
