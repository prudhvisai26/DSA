# Longest Palindromic Substring
# Given a string s, return the longest palindromicsubstring in s.

"""
Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
"""
def longestPalindrome(s):
    n=len(s)
    start=0
    end=1
    for i in range(n):
        low=i-1
        high=i
        while low>=0 and high<n and s[low]==s[high]:
            if high-low+1>end:
                start=low
                end=high-low+1
            low-=1
            high+=1
        
        low=i-1
        high=i+1
        while low>=0 and high<n and s[low]==s[high]:
            if high-low+1>end:
                start=low
                end=high-low+1
            low-=1
            high+=1
    # print(start,end)
    return s[start:start+end]