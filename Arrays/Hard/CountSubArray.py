# Count the number of subarrays with given xor K
# Problem Statement: Given an array of integers A and an integer B. Find the total number of subarrays having bitwise XOR of all elements equal to k.

"""
Example 1:
Input Format: A = [4, 2, 2, 6, 4] , k = 6
Result: 4
Explanation: The subarrays having XOR of their elements as 6 are  [4, 2], [4, 2, 2, 6, 4], [2, 2, 6], [6]

Example 2:
Input Format: A = [5, 6, 7, 8, 9], k = 5
Result: 2
Explanation: The subarrays having XOR of their elements as 5 are [5] and [5, 6, 7, 8, 9]
"""
# Approaches:
"""
1.Brute-Force:
    # Generate Subarrays: 
        # First, we will run a loop(say i) that will select every possible starting index of the subarray. The possible starting indices can vary from index 0 to index n-1(n = size of the array).
        # Inside the loop, we will run another loop(say j) that will signify the ending index of the subarray. For every subarray starting from the index i, the possible ending index can vary from index i to n-1(n = size of the array).
    # Calculate XOR of the subarray: 
        After that for each subarray starting from index i and ending at index j (i.e. arr[i….j]), we will run another loop to calculate the XOR of all the elements(of that particular subarray).
    # Check the XOR and modify the count: 
        If the XOR is equal to k, we will increase the count by 1.
    TC:O(n^3) Sc:O(1)
2.Better Approach:
    # Generate Subarrays: 
        # First, we will run a loop(say i) that will select every possible starting index of the subarray. The possible starting indices can vary from index 0 to index n-1(n = array size).
        # Inside the loop, we will run another loop(say j) that will signify the ending index as well as the current element of the subarray. For every subarray starting from the index i, the possible ending index can vary from index i to n-1(n = size of the array).
    # Calculate XOR of the subarray: 
        Inside loop j, we will XOR the current element to the XOR of the previous subarray i.e. xorr = XOR(a[i….j-1]) ^ arr[j]. 
    # Check the XOR and modify the count: 
        After calculating the XOR, we will check if the sum is equal to the given k. If it is, we will increase the value of the count.
    TC:O(n^2) SC:O(1)
3.Optimal Approach(Prefix Sum or Hashing):
    #First we declare an empty dictionary then add 0 to it with value 1,then intialize xor,count to 0.
    #Now run a loop until n and findout the xor value by updating the xor by xor^a[i]
    #Then find out the x value which xor^k(the value that need to be find out)
    #Check whether the x present in dictionary or not if it is add the value of it to count and for every iteration update dictionary with xor values.
    TC:O(n) Sc:O(n)
"""
def subarraysWithSumK(a, b):
    # Write your code here
    d={}
    d[0]=1
    xor,cnt=0,0
    for i in range(len(a)):
        xor=xor^a[i]
        x=xor^b
        if x in d:
            cnt+=d[x]
        if xor in d:
            d[xor]+=1
        else:
            d[xor]=1
    return cnt
print(subarraysWithSumK([4, 2, 2, 6, 4],6))