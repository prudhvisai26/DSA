# next_permutation : find next lexicographically greater permutation
# Problem Statement: Given an array Arr[] of integers, rearrange the numbers of the given array into the lexicographically next greater permutation of numbers.
# If such an arrangement is not possible, it must rearrange to the lowest possible order (i.e., sorted in ascending order).

"""
Example 1 :
Input format: Arr[] = {1,3,2}
Output: Arr[] = {2,1,3}
Explanation: All permutations of {1,2,3} are {{1,2,3} , {1,3,2}, {2,13} , {2,3,1} , {3,1,2} , {3,2,1}}. So, the next permutation just after {1,3,2} is {2,1,3}.

Example 2:
Input format: Arr[] = {3,2,1}
Output: Arr[] = {1,2,3}
Explanation: As we see all permutations of {1,2,3}, we find {3,2,1} at the last position. So, we have to return the topmost permutation.
"""
#Approaches:
"""
1.Brute Force:
    Step 1: Find all possible permutations of elements present and store them.
    Step 2: Search input from all possible permutations.
    Step 3: Print the next permutation present right after it.
    TC:O(N^2) SC:O(1)
2.Optimal Approach:
    #Find the breakPoint first in the given array/permutation.The breakpoint is the point where we see a decreasing sequence of numbers.
    #If breakpoint is not Found simply reverse the array that will be the result 
    #If it is exists:
        1.Find the element which is gretear than the break point element and smaller than other elements of the right half of breakpoint and swap it.
        2.Reverse the entire array from breakpoint+1 to n and return the array.
"""
def next_permutation(a):
    n=len(a)
    ind=-1
    for i in range(n-1,-1,-1):
        if a[i]>a[i-1]:
            ind=i-1
            break
    if ind==-1:
        a=a[::-1]
        return a
    for i in range(n-1,ind,-1):
        if a[i]>a[ind]:
            a[i],a[ind]=a[ind],a[i]
            break
    a[ind+1:]=reversed(a[ind+1:])
    return a
print(next_permutation([1,5,1]))