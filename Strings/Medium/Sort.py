# Sort Characters By Frequency

# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.
# Return the sorted string. If there are multiple answers, return any of them.

"""
Example 1:
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:
Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.
"""

#Approach:
"""
#Take a dictionay and add the frequency of every character of given string.
#Then sort the dictionary by key(character) in decending order.
#Now make a new string and append all the characters according to their frequencies.
TC:O(nlogn)+O(len(dict)) SC:O(n)
"""

def frequencySort(s):
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    sortedDict=sorted(d.items(),key=lambda x:x[1],reverse=True)
    # print(sortedDict)
    res=''
    for val in sortedDict:
        res+=val[0]*val[1]
    # print(res)
    return res