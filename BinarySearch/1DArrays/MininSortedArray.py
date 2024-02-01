# Minimum in Rotated Sorted Array
# Problem Statement: Given an integer array arr of size N, sorted in ascending order (with distinct values). Now the array is rotated between 1 to N times which is unknown. Find the minimum element in the array. 

"""
Example 1:
Input Format: arr = [4,5,6,7,0,1,2,3]
Result: 0
Explanation: Here, the element 0 is the minimum element in the array.

Example 2:
Input Format: arr = [3,4,5,1,2]
Result: 1
Explanation: Here, the element 1 is the minimum element in the array.
"""

def findMin(a,n,x):
    low,high=0,n-1
    mini=float('inf')
    while(low<=high):
        mid=(low+high)//2
        if a[low]<=a[high]:
            mini=min(mini,a[low])
            break
        if a[low]<=a[mid]:
            mini=min(mini,a[low])
            low=mid+1
        else:
            mini=min(mini,a[mid])
            high=mid-1
    return mini