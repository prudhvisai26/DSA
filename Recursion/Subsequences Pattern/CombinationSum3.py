"""
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.

Example 2:
Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.

"""

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def backtrack(n, ds, next):
            if n == 0 and len(ds) == k:
                res.append(ds[:])
                return
            elif n < 0 or len(ds) == k:
                return
            for i in range(next, 9):
                ds.append(i+1)
                backtrack(n-i-1, ds, i+1)
                ds.pop()
        backtrack(n, [], 0)
        return res
