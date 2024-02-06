# Count With K Different Characters

# Problem statement
# You are given a string 'str' of lowercase alphabets and an integer 'k' .
# Your task is to return the count all the possible substrings that have exactly 'k' distinct characters.

# For example:
# 'str' = abcad and 'k' = 2. 
# We can see that the substrings {ab, bc, ca, ad} are the only substrings with 2 distinct characters. 
# Therefore, the answer will be 4.    

"""
# Sample Input 1 :
# aacfssa    
# 3
# Sample Output 1 :
# 5    
# Explanation of The Sample Input 1:
# Given 'str' = “aacfssa”. We can see that the substrings with only 3 distinct characters are {aacf, acf, cfs, cfss, fssa}. 

"""

#Approach:
"""
Just count all the subarrays with at most K distinct values and k-1 distinct values then subtract the values of both to get the result.

#Fistly, we take a dictionary and  fill it with counts for each character in the input string.
#Now run a loop until length of dictionary is greater than k:
    #We will decrement  the value of last element in dictionary by one and if the value becomes zero then we remove that element and increment the left pointer to 1
    #Finally we update the result and return it.
    #Same goes for the k-1 distinct values.
TC:O(n)*O(k-1) SC:O(n)
"""

def result(s,k):
    if s=="":
        return 0
    char_count={}
    res=0
    left=0
    for i in range(len(s)):
        if s[i] in char_count:
            char_count[s[i]]+=1
        else:
            char_count[s[i]]=1
        while len(char_count)>k:
            char_count[s[left]]-=1
            if char_count[s[left]]==0:
                char_count.pop(s[left])
            left+=1
        res+=i-left+1
    return res
def countSubStrings(s: str, k: int) -> int:
    # Write your code here
    return result(s,k)-result(s,k-1)