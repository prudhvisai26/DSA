"""
Problem statement
You are given an array 'A' of size 'N' and an integer'K'’. You need to generate and return all subarrays of array ‘A’ whose sum = ‘K’.

Note: In the output, you will see the 2D array lexicographically sorted.

Example:
Input: ‘N’ = 6 ‘K’ = 3
‘A’ = [1, 2, 3, 1, 1, 1]
Output: 3
Explanation: Subarrays whose sum = ‘3’ are:
[1, 2], [3], and [1, 1, 1]

Sample Input 1:
6 3
1 2 3 1 1 1
Sample Output 1:
3
Explanation Of Sample Input 1:
Input: ‘N’ = 6 ‘K’ = 3
‘A’ = [1, 2, 3, 1, 1, 1]
Output: 3
Explanation: Subarrays whose sum = ‘3’ are:
[1, 2], [3], and [1, 1, 1]

"""
from copy import deepcopy;
def subarraysWithSumK( a:[list], k:int) ->[[int]]:
    # Write your code here
    n=len(a)
    ans=[]
    for i in range(n):
        sub=[a[i]]
        if a[i]==k:
            ans.append(sub)
            continue
        else:
            for j in range(i+1,n):
                sub.append(a[j])
                if sum(sub)==k:
                    ans.append(sub)
                    break
    return ans
