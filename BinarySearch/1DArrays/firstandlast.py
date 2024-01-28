# First and Last Occurrences in Array
# Problem Statement: Given a sorted array arr of n integers and a target value k. Write a program to find the indices of the first and the last occurrences of the target value. If the target is not found then return -1 as indices.

"""
Example 1:
Input Format: n = 8, arr[] = {2, 4, 6, 8, 8, 8, 11, 13}, k = 8
Result: 3 5
Explanation: The first occurrence of 8 is at index 3 and the last occurrence is at index 5.

Example 2:
Input Format: n = 8, arr[] = {2, 4, 6, 8, 8, 8, 11, 13}, k = 10
Result: -1 -1
Explanation: The target value is not present in the array. So, we have returned -1 as the indices of the first and the last occurrence.
"""

# Code:
def firstPosition(a,n,k):
    low,high,ans=0,n-1,-1
    while(low<=high):
        mid=(low+high)//2
        if a[mid]==k:
            ans=mid
            high=mid-1
        elif a[mid]<k:
            low=mid+1
        else:
            high=mid-1
    return ans
def secondPosition(a,n,k):
    low,high,ans=0,n-1,-1
    while low<=high:
        mid=(low+high)//2
        if a[mid]==k:
            ans=mid
            low=mid+1
        elif a[mid]<k:
            low=mid+1
        else:
            high=mid-1
    return ans
def firstAndLastPosition(arr,n,k):
    f=firstPosition(arr,n,k)
    s=secondPosition(arr,n,k)
    return (f,s)