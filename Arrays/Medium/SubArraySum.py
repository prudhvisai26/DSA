# Count Subarray sum Equals K
# Problem Statement: Given an array of integers and an integer k, return the total number of subarrays whose sum equals k.

# A subarray is a contiguous non-empty sequence of elements within an array.

"""
Example 1:
Input Format: N = 4, array[] = {3, 1, 2, 4}, k = 6
Result: 2
Explanation: The subarrays that sum up to 6 are [3, 1, 2] and [2, 4].

Example 2:
Input Format: N = 3, array[] = {1,2,3}, k = 3
Result: 2
Explanation: The subarrays that sum up to 3 are [1, 2], and [3].
"""
#Approaches:
"""
1.BruteForce:
    #Run two loops (from 0 to n) and (i to n)
    #Now take a sum variable and add the sum from a[i:j+1]
    #Now check that sum with k if it is equals then increment the count.
    TC:O(n*3) Sc:O(1)
2.Better Approach:
    #Run nested loops as in brute force now take a sum variable and initialize to 0 for every ith iteration.
    #Add current element to sum and check this sum with k if it is equal to k then increment the count 
    TC:O(n*2) Sc:O(1)
3.Optimal Approach (HashMap and PreSum):
    #Initialize a hash map and add (0,1) which is prefix sum,count in it.
    #Then run a loop and add the current element to prefix sum variable.
    #Now calculate the remaining sum which is presum-k and check it in the hashmap if it there then add the count or value to the cnt var
    #add the remaining part to dictionary with the appropriate value.
    TC:O(N) Sc:O(1)
 """

def subarraySum(a,k):
    n=len(a)
    preSum,cnt=0,0
    d={}
    d[0]=1
    for i in range(n):
        preSum+=a[i]
        rem=preSum-k
        if rem in d:
            cnt+=d[rem]
        if preSum in d:
            d[preSum]+=1
        else:
            d[preSum]=1
    return cnt
print(subarraySum([1,2,3,-3,1,1,1,4,2,-3],3)) 
