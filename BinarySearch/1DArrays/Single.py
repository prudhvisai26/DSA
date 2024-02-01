# Search Single Element in a sorted array
# Problem Statement: Given an array of N integers. Every number in the array except one appears twice. Find the single number in the array.

"""
Example 1:
Input Format: arr[] = {1,1,2,2,3,3,4,5,5,6,6}
Result: 4
Explanation: Only the number 4 appears once in the array.

Example 2:

Input Format: arr[] = {1,1,3,5,5}
Result: 3
Explanation: Only the number 3 appears once in the array.
"""

#EvenOdd Approach:

def singleNonDuplicate(nums):
    # Write your code here
    n=len(nums)
    if n==1:
        return nums[0]
    if nums[0]!=nums[1]:
        return nums[0]
    if nums[n-1]!=nums[n-2]:
        return nums[n-1]
    low,high=1,n-2
    while(low<=high):
        mid=(low+high)//2
        if nums[mid]!=nums[mid+1] and nums[mid]!=nums[mid-1]:
            return nums[mid]
        if (mid%2==0 and nums[mid]==nums[mid+1]) or (mid%2!=0 and nums[mid]==nums[mid-1]):
            low=mid+1
        else:
            high=mid-1
    return -1