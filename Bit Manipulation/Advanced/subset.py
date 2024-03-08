"""

Given an integer array nums of unique elements, return all possible subsets(the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
"""

def subsets(self, nums: List[int]) -> List[List[int]]:
    ans,n=[],len(nums)
    m=(1<<n)
    for num in range(m):
        a=[]
        for i in range(0,n):
            if(num&(1<<i)):
                a.append(nums[i])
        ans.append(a)
    return ans
