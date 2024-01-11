"""
Example 1:
Input: N = 5, array[] = {1,2,3,4,5}
Output: True.
Explanation: The given array is sorted i.e Every element in the array is smaller than or equals to its next values, So the answer is True.

Example 2:
Input: N = 5, array[] = {5,4,6,7,8}
Output: False.
Explanation: The given array is Not sorted i.e Every element in the array is not smaller than or equal to its next values, So the answer is False.
Here element 5 is not smaller than or equal to its future elements.

"""

#Approaches:
"""
1.Brute Force:
    #Just check if the present element is less than the next element by having a nested loop return True else False
2.Single Traversal:
    #Traverse through the array and check if the present element is greater than the next element return false else true 
"""

def isSorted(a):
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            return False
    return True

print(isSorted([1,9,3,4,5]))



##----Check if Array Is Sorted and Rotated

"""
Example 1:

Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 3 positions to begin on the the element of value 3: [3,4,5,1,2].
Example 2:

Input: nums = [2,1,3,4]
Output: false
Explanation: There is no sorted array once rotated that can make nums.
"""

def check(a):
    c=0
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            c+=1
    if a[0]<a[len(a)-1]:
        c+=1
    return c<=1

print(check([2,1,3,4]))