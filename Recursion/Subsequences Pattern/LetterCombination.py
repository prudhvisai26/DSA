"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
"""

def letterCombinations(self, digits: str) -> List[str]:
    if not digits:
        return []
    d={'2': 'abc','3': 'def','4': 'ghi','5': 'jkl','6': 'mno','7': 'pqrs','8': 'tuv','9': 'wxyz'}
    ans=[]
    
    def backtrack(c,s):
        if len(s)==0:
            ans.append(c)
        else:
            for l in d[s[0]]:
                backtrack(c+l,s[1:])
    backtrack("",digits)
    return ans
