"""
Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mpp=[-1]*256
        left,right=0,0
        length=0
        while right<len(s):
            if mpp[ord(s[right])]!=-1:
                left=max(mpp[ord(s[right])]+1,left)
            mpp[ord(s[right])]=right
            length=max(length,right-left+1)
            right+=1
        return length
