"""
Problem statement
You are given an array 'arr' of length ‘N’.
Let ‘X’ be the minimum element of any contiguous subarray of ‘arr’.
You need to return the sum of 'X' over all the contiguous subarrays of 'arr'. Since the answer may be large, you should return it modulo 10^9+7.
A contiguous subarray is a subset of consecutive elements from an array where the elements are adjacent and appear in the same order as in the original array.

Example:
Input:
arr = [1, 2, 3, 4], N = 4
Output:
20

Explanation: Valid contiguous subarrays are [1], [2], [3], [4], [1, 2], [2, 3], [3, 4], [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4]. 
The minimum number in the subarrays are 1, 2, 3, 4, 1, 2, 3, 1, 2 and 1.
The sum of these minimum numbers is 20.
Hence we return 20.

Sample Input 1:
3
1 5 3
Sample Output 1:
14
Explanation Of Sample Input 1:
For test case one:
Input:
arr = [1, 5, 3], N=3
Output:
14
Explanation: Valid contiguous subarrays are [1], [5], [3], [1, 5], [5, 3], and [1, 5, 3]. 
The minimum number in the subarrays are 1, 5, 3, 1, 3, and 1.
The sum of these minimum numbers is 14.
Hence we return 14.
"""

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n=len(arr)
        left=[0]*n
        right=[0]*n
        s1,s2=[],[]
        mod=10**9+7
        for i in range(n):
            cnt=1
            while s1 and s1[-1][0]>arr[i]:
                cnt+=s1[-1][1]
                s1.pop()
            s1.append([arr[i],cnt])
            left[i]=cnt
        for i in range(n-1,-1,-1):
            cnt=1
            while s2 and s2[-1][0]>=arr[i]:
                cnt+=s2[-1][1]
                s2.pop()
            s2.append([arr[i],cnt])
            right[i]=cnt
        res=0
        for i in range(n):
            res+=(arr[i]*(left[i]*right[i]))%mod
        return res%mod
