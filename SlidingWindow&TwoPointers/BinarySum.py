"""
Binary Subarrays With Sum

Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.
A subarray is a contiguous part of the array.

Example 1:
Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]

Example 2:
Input: nums = [0,0,0,0,0], goal = 0
Output: 15
"""

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count={0:1}
        sum=0
        res=0
        for i in nums:
            sum+=i
            if sum-goal in count:
                res+=count[sum-goal]
            count[sum]=count.get(sum,0)+1
        return res
