# Count Occurrences in Sorted Array
# Problem Statement: You are given a sorted array containing N integers and a number X, you have to find the occurrences of X in the given array.

"""
Example 1:
Input: N = 7,  X = 3 , array[] = {2, 2 , 3 , 3 , 3 , 3 , 4}
Output: 4
Explanation: 3 is occurring 4 times in 
the given array so it is our answer.

Example 2:
Input: N = 8,  X = 2 , array[] = {1, 1, 2, 2, 2, 2, 2, 3}
Output: 5
Explanation: 2 is occurring 5 times in the given array so it is our answer.
"""
#Approach:
"""
We can use Binary Search to find the element first and then count its occurrence using two pointers approach.
# LastOccurence-FirstOccurence+1
"""

def firstOccurence(a,n,x):
    low,high,ans=0,n-1,-1
    while low<=high:
        mid=(low+high)//2
        if a[mid]==x:
            ans=mid
            high=mid-1
        elif a[mid]>x:
            high=mid-1
        else:
            low=mid+1
    return ans

def lastOccurence(a,n,x):
    low,high,ans=0,n-1,-1
    while(low<=high):
        mid=(low+high)//2
        if a[mid]==x:
            ans=mid
            low=mid+1
        if a[mid]<x:
            low=mid+1
        else:
            high=mid-1
    return ans

def count(a,n,x):
    first=firstOccurence(a,n,x)
    second=lastOccurence(a,n,x)
    if first==-1:
        return 0
    return second-first+1