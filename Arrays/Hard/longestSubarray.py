# Length of the longest subarray with zero Sum
# Problem Statement: Given an array containing both positive and negative integers, we have to find the length of the longest subarray with the sum of all elements equal to zero.

"""
Example 1:
Input Format: N = 6, array[] = {9, -3, 3, -1, 6, -5}
Result: 5
Explanation: The following subarrays sum to zero:
{-3, 3} , {-1, 6, -5}, {-3, 3, -1, 6, -5}
Since we require the length of the longest subarray, our answer is 5!

Example 2:
Input Format: N = 8, array[] = {6, -2, 2, -8, 1, 7, 4, -10}
Result: 8
Subarrays with sum 0 : {-2, 2}, {-8, 1, 7}, {-2, 2, -8, 1, 7}, {6, -2, 2, -8, 1, 7, 4, -10}
Length of longest subarray = 8

Example 3:
Input Format: N = 3, array[] = {1, 0, -5}
Result: 1
Subarray : {0}
Length of longest subarray = 1

"""
# Approaches:
"""
1.Brute-Force:
    # Initialize a variable max = 0, which stores the length of the longest subarray with a sum of 0.
    # Traverse the array from the start and initialize a variable sum = 0 which stores the sum of the subarray starting with the current index
    # Traverse from the next element of current_index up to the end of the array, each time add the element to the sum and check if it is equal to 0.
    # If sum = 0, check if the length of the subarray so far is > max and if yes update max
    # Now keep adding elements and repeat step 3 a.
    # After the outer loop traverses all elements return max
    TC:O(n^2) SC:O(1)
2.Optimal Approach(Prefix Sum):
    # First, let us initialize a variable say sum = 0 which stores the sum of elements traversed so far and another variable says max = 0 which stores the length of the longest subarray with sum zero.
    # Declare a HashMap<Integer, Integer> which stores the prefix sum of every element as a key and its index as a value.
    # Now traverse the array, and add the array element to our sum. 
    # If sum = 0, then we can say that the subarray until the current index has a sum = 0,so we update max with the maximum value of (max, current_index+1)
    #If the sum is not equal to zero then we check the hashmap if we havve seen a subarray with this sum before
    # if HashMap contains sum -> this is where the above-discussed case occurs (subarray with equal sum), so we update our max 
    # else -> Insert (sum, current_index) into hashmap to store prefix sum until the current index
    # After traversing the entire array our max variable has the length of the longest substring having a sum equal to zero, so return max.
    TC:O(n) SC:O(n)
"""
def getLongestZeroSumSubarrayLength(arr ):
    sum,maxi=0,0
    d={}
    for i in range(len(arr)):
        sum+=arr[i]
        if sum==0:
            maxi=i+1
        else:
            if sum in d:
                maxi=max(maxi,i-d[sum])
            else:
                d[sum]=i
    return maxi
print(getLongestZeroSumSubarrayLength([6, -2, 2, -8, 1, 7, 4, -10]))
