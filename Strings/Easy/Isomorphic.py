#Isomorphic Strings

# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

"""
Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false
"""

#Approach(Hashing):
"""
#First we check if length of strings are equal or not.It it doesn't then there  is no chance for them to be isomorphic so return False.
#We will create a hashmap for each string where keys represent character of 's' and values represent corresponding character of 't' 
#Now we check if the key of string s is already present in value of t then we will return False.
#If both of them not present we simply update the dict values of both strings
#Else we check whether the current  haracter of string s matches with the value at its key in dictionary or not.
TC:O(n) SC:O(n)+O(n)
"""

def isIsomorphic(s,t):
    if(len(s)!=len(t)):
        return False
    d={}
    r={}
    for i in range(len(s)):
        if s[i] not in d:
            if t[i] in r:
                return False
            d[s[i]]=t[i]
            r[t[i]]=s[i]
        else:
            if d[s[i]]!=t[i]:
                return False
    # print(d)
    return True