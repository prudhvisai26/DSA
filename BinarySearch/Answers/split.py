# Split Array – Largest Sum
# Problem Statement: Given an integer array ‘A’ of size ‘N’ and an integer ‘K’. Split the array ‘A’ into ‘K’ non-empty subarrays such that the largest sum of any subarray is minimized. Your task is to return the minimized largest sum of the split.
# A subarray is a contiguous part of the array.

"""
Example 1:
Input Format: N = 5, a[] = {1,2,3,4,5}, k = 3
Result: 6
Explanation: There are many ways to split the array a[] into k consecutive subarrays. The best way to do this is to split the array a[] into [1, 2, 3], [4], and [5], where the largest sum among the three subarrays is only 6.

Assume the given array is {10, 20, 30, 40} and k = 2. Now, we can split the array in the following ways:
10 | 20, 30, 40  → Maximum subarray sum  = 90
10, 20 | 30, 40  → Maximum subarray sum = 70
10, 20, 30 | 40  → Maximum subarray sum = 60

From the above allocations, we can clearly observe that in the last case, the maximum subarray sum is the minimum possible. So, 60 will be the answer.
Observations:
    Minimum possible answer: We will get the minimum answer when we split the array into n subarrays(i.e. Each subarray will have a single element). Now, in this case, the maximum subarray sum will be the maximum element in the array. So, the minimum possible answer is max(arr[]).
    Maximum possible answer: We will get the maximum answer when we put all n elements into a single subarray. The maximum subarray sum will be the summation of array elements i.e. sum(arr[]). So, the maximum possible answer is sum(arr[]).

From the observations, it is clear that our answer lies in the range [max(arr[]), sum(arr[])].

How to calculate the number of subarrays we need to make if the maximum subarray sum can be at most ‘maxSum’:
In order to calculate the number of subarrays we will write a function, countPartitions(). This function will take the array and ‘maxSum’ as parameters and return the number of partitions.

countPartitions(arr[], maxSum):
We will first declare two variables i.e. ‘partitions’(stores the no. of partitions), and ‘subarraySum’(stores the sum of the current subarray). As we are starting with the first subarray, ‘partitions’ should be initialized with 1.
We will start traversing the given array.
If subarraySum + arr[i] <= maxSum: If upon adding the current element with ‘subarraySum’ does not exceed ‘maxSum’, we can insert this i-th element to the current subarray.
Otherwise, we will move to the next subarray(i.e. partitions += 1 ) and insert the i-th element into that.
Finally, we will return the value of ‘partitions’.
"""
def count(a,s):
    n=len(a)
    p=1
    sum=0
    for i in range(n):
        if sum+a[i]>s:
            p+=1
            sum=a[i]
        else:
            sum+=a[i]
    return p
def largestSubarraySumMinimized(a: [int], k: int) -> int:
    # Write Your Code Here
    low=max(a)
    high=sum(a)
    while(low<=high):
        mid=(low+high)//2
        partitions=count(a,mid)
        if partitions<=k:
            high=mid-1
        else:
            low=mid+1
    return low