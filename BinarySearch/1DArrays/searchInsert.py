# Problem Statement: You are given a sorted array arr of distinct values and a target value x. You need to search for the index of the target value in the array.
# If the value is present in the array, then return its index. Otherwise, determine the index where it would be inserted in the array while maintaining the sorted order.

"""
Example 1:
Input Format: arr[] = {1,2,4,7}, x = 6
Result: 3
Explanation: 6 is not present in the array. So, if we will insert 6 in the 3rd index(0-based indexing), the array will still be sorted. {1,2,4,6,7}.

Example 2:
Input Format: arr[] = {1,2,4,7}, x = 2
Result: 1
Explanation: 2 is present in the array and so we will return its index i.e. 1.
"""

#Approaches:
"""
# Place the 2 pointers i.e. low and high: Initially, we will place the pointers like this: low will point to the first index and high will point to the last index.
# Calculate the ‘mid’: Now, we will calculate the value of mid using the following formula:
# mid = (low+high) // 2 ( ‘//’ refers to integer division)
# Compare arr[mid] with x: With comparing arr[mid] to x, we can observe 2 different cases:
# Case 1 – If arr[mid] >= x: This condition means that the index mid may be an answer. So, we will update the ‘ans’ variable with mid and search in the left half if there is any smaller index that satisfies the same condition. Here, we are eliminating the right half.
# Case 2 – If arr[mid] < x: In this case, mid cannot be our answer and we need to find some bigger element. So, we will eliminate the left half and search in the right half for the answer.
"""

def searchInsert(a,n,x):
    low,high,res=0,n-1,n
    while(low<=high):
        mid=(low+high)//2
        if a[mid]>=x:
            res=mid
            high=mid-1
        else:
            low=mid+1
    return res
