# Kadane’s Algorithm : Maximum Subarray Sum in an Array
# Problem Statement: Given an integer array arr, find the contiguous subarray (containing at least one number) which ha0s the largest sum and returns its sum and prints the subarray.

"""
Example 1:
Input: arr = [-2,1,-3,4,-1,2,1,-5,4] 
Output: 6 
Explanation: [4,-1,2,1] has the largest sum = 6. 

Examples 2: 
Input: arr = [1] 
Output: 1 
Explanation: Array has only one element and which is giving positive sum of 1. 
"""
#Approaches:
"""
1.Brute Force:  
    #First, we will run a loop(say i) that will select every possible starting index of the subarray. The possible starting indices can vary from index 0 to index n-1(n = size of the array).
    #Inside the loop, we will run another loop(say j) that will signify the ending index of the subarray. For every subarray starting from the index i, the possible ending index can vary from index i to n-1(n = size of the array).
    #After that for each subarray starting from index i and ending at index j (i.e. arr[i….j]), we will run another loop to calculate the sum of all the elements(of that particular subarray).
2.Approach 1(Kadane Algo):
    #We will run a loop to iterate the given array.
    #Now we will find the sum from first element.
        1.if the sum>maxi update maxi
        2.if sum<0 update sum to 0 with that we can only get the maximum sun of the array by negating the negative elements.
    TC:O(n) Sc:O(1)
3.FollowUp Question: Print the subArray with Max Sum:
    #Here we just add some variables to previous algo like start,startindex and endindex
    #Whenever we get sum as 0 we update start variable because whenever we get the sum as 0 the subarray starts there.
    #If sum >maxSum:
        1.We will update maxSum and update startindex to start and endindex to i.
    #Finally we fetch out the indecies and print the array of elements for that.
"""

def maxSubArray(a):
    sum,maxi=0,float('-inf')
    for i in a:
        sum+=i
        if sum>maxi:
            maxi=sum
        if sum<0:
            sum=0
    return maxi
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

def printMaxSubArray(a):
    n=len(a)
    sum,maxi=0,float('-inf')
    start,s,e=0,-1,-1
    for i in range(n):
        if sum==0:
            start=i
        sum+=a[i]
        if sum>maxi:
            maxi=sum
            s=start
            e=i
        if sum<0:
            sum=0
    return a[s:e+1]
print(printMaxSubArray([-2,1,-3,4,-1,2,1,-5,4]))