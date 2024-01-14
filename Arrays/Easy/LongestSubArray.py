#Longest Subarray with given Sum K(Positives)
# Problem Statement: Given an array and a sum k, we need to print the length of the longest subarray that sums to k.

"""
Example :
Input: n= 7 k= 3
a= [1, 2, 3, 1, 1, 1, 1]
Output: 3
Explanation: Subarrays whose sum = 3 are:
[1, 2], [3], [1, 1, 1]
Here, the length of the longest subarray is 3, which is our final answer.

Example 2:
Input Format: N = 5, k = 10, array[] = {2,3,5,1,9}
Result: 3
Explanation: The longest subarray with sum 10 is {2, 3, 5}. And its length is 3.
"""
#Approaches:
"""
1.Brute Force:
    #Run nested loops with var sum intialized to 0.
    #Now in the inner loop for each i increment sum with a[j] and find out if the sum is equal to k
    #if it is equal then length will max(length,i+j-1)
    TC:O(n^2) SC:O(1)
2.Optimal Approach (works for only positives) Two pointers:
    #Initialize a maxlength,i,j with 0 and sum with a[0]
    #Now run a loop until n and inside run another loop whether the sum greater than k if it is then decrement the sum value with a[i]
    #Then check if the sum==k then update max then increment sum until j reaches n
    TC:O(n) Sc:O(1) 
3.Optimal Approach (works for positives and negatives) preSum:
    #First, we will declare a map to store the prefix sums and the indices.
    # Then we will run a loop(say i) from index 0 to n-1(n = size of the array).
    # For each index i, we will do the following:
    # We will add the current element i.e. a[i] to the prefix sum.
    # If the sum is equal to k, we should consider the length of the current subarray i.e. i+1. We will compare this length with the existing length and consider the maximum one.
    # We will calculate the prefix sum i.e. x-k, of the remaining subarray.
    # If that sum of the remaining part i.e. x-k exists in the map, we will calculate the length i.e. i-preSumMap[x-k], and consider the maximum one comparing it with the existing length we have achieved until now.
    # If the sum, we got after step 3.1, does not exist in the map we will add that with the current index into the map. We are checking the map before insertion because we want the index to be as minimum as possible and so we will consider the earliest index where the sum x-k has occurred. [Detailed discussion in the edge case section]
    # In this approach, we are using the concept of the prefix sum to solve this problem. Here, the prefix sum of a subarray ending at index i, simply means the sum of all the elements of that subarray.
    TC:O(n) Sc:O(n)

"""
def Longest_Subarray_with_given_Sum(a,k):
    n=len(a)
    i,j,maxi=0,0,0
    sum=a[0]
    while(j<n):
        while(i<=j and sum>k):
            sum=sum-a[i]
            i+=1
        if(sum==k):
            maxi=max(maxi,j-i+1)
        j+=1
        if j<n:
            sum+=a[j]
    return maxi
print(Longest_Subarray_with_given_Sum([2,3,5,1,9],10))

def Longest_SubArray(a,k):
    n=len(a)
    prefix_Sum={}
    sum,maxi=0,0
    for i in range(n):
        sum+=a[i]
        if(sum==k):
            maxi=max(maxi,i+1)
        rem=sum-k
        if rem in prefix_Sum:
            l=i-prefix_Sum[rem]
            maxi=max(maxi,l)
        if sum not in prefix_Sum:
            prefix_Sum[sum]=i
    return maxi
print(Longest_SubArray([1, 2, 3, 1, 1, 1, 1],0))