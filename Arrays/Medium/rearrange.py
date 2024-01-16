# Rearrange Array Elements by Sign
# Problem Statement:
# There’s an array ‘A’ of size ‘N’ with an equal number of positive and negative elements. Without altering the relative order of positive and negative elements, you must return an array of alternately positive and negative values.
# Note: Start the array with positive elements.

"""
Example :
Input:
arr[] = {1,2,-3,-1,-2,-3}, N = 6
Output:
1 -3 2 -1 3 -2
Explanation: 
Positive elements = 1,2,3
Negative elements = -3,-1,-2
To maintain relative ordering, 1 must occur before 2, and 2 must occur before 3.
Also, -3 should come before -1, and -1 should come before -2.

"""

def rearrangeArray(nums):
    n=len(nums)
    a=[0]*n
    pos,neg=0,1
    for i in range(n):
        if nums[i]>=0:
            a[pos]=nums[i]
            pos+=2
        else:
            a[neg]=nums[i]
            neg+=2
    return a