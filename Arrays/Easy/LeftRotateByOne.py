#LeftRotateByOne

#Problem Statement: Given an array of N integers, left rotate the array by one place.
"""
Example 1:
Input: N = 5, array[] = {1,2,3,4,5}
Output: 2,3,4,5,1
Explanation: 
Since all the elements in array will be shifted toward left by one so 2 will now become the first index and and 1 which was present at first index will be shifted at last.
"""
#Approaches:
"""
1.Brute Force:
    #Take an temp array and just append the elements from index 1 to n then at last append the 0th index in temp array.
    TC:O(n) SC:O(n)
2.Optimal Approach:
    #First take a temp var and initialize it to first element of the array.
    #Now run a loop from 1 to n and update a[i-1]=a[i]
    #Atlast update the last element with the temp.
"""
def LeftRotateByOne(a):
    temp=a[0]
    for i in range(1,len(a)):
        a[i-1]=a[i]
    a[len(a)-1]=temp
    return a
print(LeftRotateByOne([1,2,3,4,5]))