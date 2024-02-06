#Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

"""
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""
 
#Approach:
"""
1.Sort the Array containing strings.
2.Take first and last strings length in the array and have a loop until the characters of first string and last string are equal.
3.If it is equal then increment the i,.
TC:O(nlogn)+O(min(len(s[0]),len(s[-1]))) ,SC:O(1)
"""

def longestCommonPrefix(s):
    s.sort()
    if(len(s)==1):
        return s[0]
    i=0
    while(i<len(s[0]) and i<len(s[-1]) and s[0][i]==s[-1][i]):
        i+=1
    return s[0][:i]