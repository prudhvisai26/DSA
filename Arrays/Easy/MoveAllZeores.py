# MoveAllZeores

#Move all Zeros to the end of the array
"""
#Problem Statement: You are given an array of integers, your task is to move all the zeros in the array to the end of the array and move 
#non-negative integers to the front by maintaining their order.

Input: 1 ,0 ,2 ,3 ,0 ,4 ,0 ,1
Output: 1 ,2 ,3 ,4 ,1 ,0 ,0 ,0
Explanation: All the zeros are moved to the end and non-negative integers are moved to front by maintaining order

"""
#Approaches:
"""
1.Approach-1:
    #Take an empty array and append the all non-zero elements into the array.
    #Finally,append zeroes at the end of the array.
    Time Complexity:O(n) SC:O(n)
2.Approach-2 (2-Pointers):
    #First intialize a variable let say j to -1 and find out the first zero index in the array.
    #Then iterate the array from j+1 to n and find out the non-zero element in the array.
    #Now swap those values and increment the j to next position.
"""
def moveZeroes(a):
    j,n=-1,len(a)
    for i in range(n):
        if a[i]==0:
            j=i
            break
    if j==-1:
        return a
    for i in range(j+1,n):
        if a[i]!=0:
            a[i],a[j]=a[j],a[i]
            j+=1
    return a
print(moveZeroes([0,2,0,3,0,0,0]))