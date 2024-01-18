# Longest Consecutive Sequence in an Array
# Problem Statement: You are given an array of ‘N’ integers. You need to find the length of the longest sequence which contains the consecutive elements.

"""
Example:

Input: [100, 200, 1, 3, 2, 4]
Output: 4
Explanation: The longest consecutive subsequence is 1, 2, 3, and 4.

Input: [3, 8, 5, 7, 6]
Output: 4
Explanation: The longest consecutive subsequence is 5, 6, 7, and 8.
"""

#Approaches:
"""
1.BruteForce:
    #Take two loops and set longest var to 1 and cnt to 1 for each iteration.
    #Now run a while loop and do a linear search for each element until it found x+1 element in the array.
    #Whenever you get the element increment count and update longest var
    #Repeat the process untill you found the longest length.
    TC:O(n^2) SC:O(1)
2.Approach 2:
    #Sort the array then intiliaze the cnt,lastsmaller and max variables
    #Now iterate the array annd check whether the element-1 === last smaller if it is then update count and lastmsaller to a[i]
    #if the element not equal to lastsmaller update count=1 and lastsmaller to a[i]
    #For each iteration update longest length using max.
    TC:O(nlong)+O(n) Sc:O(1)
3.Optimal Approach(Using Sets):
    #Declare a set and add the array elements to set.
    #Now iterate the set and check whether the ele-1 in set or not if it is:
        1.Initialize cnt=1 and let x=it
        2.run a while loop until x+1 in set and do the below operations in while loop
        3.increment cnt,x and update max value after the while loop
    TC:O(n)+O(2*N) SC:O(n)
"""

def longestConsecutive(a):
    if len(a)==0:
        return 0
    s=set(a)
    longest=1
    for i in s:
        if i-1 not in s:
            cnt=1
            x=i
            while x+1 in s:
                cnt+=1
                x+=1
            longest=max(longest,cnt)
    return longest
print(longestConsecutive([100,4,200,1,3,2]))