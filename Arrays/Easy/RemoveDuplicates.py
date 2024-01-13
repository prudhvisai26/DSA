#Question:
"""
Problem Statement: Given an integer array sorted in non-decreasing order, remove the duplicates in place such that each unique element appears only once. The relative order of the elements should be kept the same.
If there are k elements after removing the duplicates, then the first k elements of the array should hold the final result. It does not matter what you leave beyond the first k elements.
Note: Return k after placing the final result in the first k slots of the array.

Input: arr[1,1,1,2,2,3,3,3,3,4,4]
Output: arr[1,2,3,4,_,_,_,_,_,_,_]

Explanation: Total number of unique elements are 4, i.e[1,2,3,4] and Therefore return 4 after assigning [1,2,3,4] in the beginning of the array.
"""

#Approaches:
"""
1. Brute Force:
    #Take a set and add the elements of array in it then print the length of array.
    #Another approach by just taking an empty array and appending the elements from array if the array doesn't have the elements in it.
    TC:O(n) SC:O(n) for sets it will be O(nlogn)+O(n)

2. Optimal Approach (Two pointers):
    #Take 2 pointers let say i,j and initialize i to 0.
    #Now  iterate the array from 1 to n and check whether the element is equal or not i.e,
        if a[i]!=a[j] increment i and change a[i] value to a[j]
    #Then print i+1 as the length and the remaining array.
"""

#Code:
def removeDuplicates(a):
    i=0
    for j in range(1,len(a)):
        if a[i]!=a[j]:
            i+=1
            a[i]=a[j]
    return (i+1,a)
print(removeDuplicates([1,1,2,3,3,4,5,5]))