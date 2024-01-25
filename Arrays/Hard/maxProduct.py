# Maximum Product Subarray in an Array
# Problem Statement: Given an array that contains both negative and positive integers, find the maximum product subarray.

"""
Example 1:
Input:
 Nums = [1,2,3,4,5,0]
Output:
 120
Explanation:
 In the given array, we can see 1×2×3×4×5 gives maximum product value.

"""
#Approaches:
"""
1.Brute-Force:
    Find all possible subarrays of the given array. Find the product of each subarray. Return the maximum of all them.
    # Following are the steps for the approach:-
        # Run a loop on the array to choose the start point for each subarray.
        # Run a nested loop to get the end point for each subarray.
        # Multiply elements present in the chosen range.
    TC:O(N^3) SC:O(1)
2.Better Approach:
    # We can optimize the brute force by making 3 nested iterations to 2 nested iterations
    # Run a loop to find the start of the subarrays.
    # Run another nested loop
    # Multiply each element and store the maximum value of all the subarray.
    TC:O(N^2) SC:O(1)
3.Optimal Approach (Prefix and Suffix):
    # We will first declare 2 variables i.e. ‘pre’(stores the product of the prefix subarray) and ‘suff’(stores the product of the suffix subarray). They both will be initialized with 1(as we want to store the product).
    # Now, we will use a loop(say i) that will run from 0 to n-1.
    # We have to check 2 cases to handle the presence of 0:
        # If pre = 0: This means the previous element was 0. So, we will consider the current element as a part of the new subarray. So, we will set ‘pre’ to 1.
        # If suff = 0: This means the previous element was 0 in the suffix. So, we will consider the current element as a part of the new suffix subarray. So, we will set ‘suff’ to 1.
    # Next, we will multiply the elements from the starting index with ‘pre’ and the elements from the end with ‘suff’. To incorporate both cases inside a single loop, we will do the following:
        # We will multiply arr[i] with ‘pre’ i.e. pre *= arr[i].
        # We will multiply arr[n-i-1] with ‘suff’ i.e. suff *= arr[n-i-1].
    # After each iteration, we will consider the maximum among the previous answer, ‘pre’ and ‘suff’ i.e. max(previous_answer, pre, suff).
    # Finally, we will return the maximum product.
    TC:O(n) SC:O(1)
"""
def maxProduct(nums):
    pre,suff,maxi=1,1,float('-inf')
    n=len(nums)
    for i in range(n):
        if pre==0:
            pre=1
        if suff==0:
            suff=1
        pre=pre*nums[i]
        suff=suff*nums[n-i-1]
        maxi=max(maxi,max(pre,suff))
    return maxi
