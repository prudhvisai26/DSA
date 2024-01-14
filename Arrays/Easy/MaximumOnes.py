#Count Maximum Consecutive One’s in the array

#Problem Statement: Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array.

"""
Input: prices = {1, 1, 0, 1, 1, 1}
Output: 3
Explanation: There are two consecutive 1s and three consecutive 1s in the array out of which maximum is 3.

Input: prices = {1, 0, 1, 1, 0, 1} 
Output: 2
Explanation: There are two consecutive 1's in the array. 
"""
#Approaches:
"""
1.Optimal Approach:
    #Lets take 2 variables count,max and intiliaze it to 0
    #Iterate through the given list and find out if the element is equal to 1 then increase count by 1.
    #If the current number is not equal to 1 then update max with finding a max element between count and max.
    #Finally, after the completition of loop find out the maximum and print it.
    TC:O(n) SC:O(n)
"""

def MaximumOnes(a):
    n=len(a)
    maxi,count=0,0
    for i in a:
        if i==1:
            count+=1
        else:
            maxi=max(maxi,count)
            count=0
    maxi=max(maxi,count)
    return maxi
print(MaximumOnes([0,0,0,0,0,1]))