# Count inversions in an array
# Problem Statement: Given an array of N integers, count the inversion of the array.
# What is an inversion of an array? Definition: for all i & j < size of array, if i < j then you have to find pair (A[i],A[j]) such that A[j] < A[i].

"""
Example 1:
Input Format: N = 5, array[] = {1,2,3,4,5}
Result: 0
Explanation: we have a sorted array and the sorted array has 0 inversions as for i < j you will never find a pair such that A[j] < A[i]. More clear example: 2 has index 1 and 5 has index 4 now 1 < 5 but 2 < 5 so this is not an inversion.

Example 2:
Input Format: N = 5, array[] = {5,4,3,2,1}
Result: 10
Explanation: we have a reverse sorted array and we will get the maximum inversions as for i < j we will always find a pair such that A[j] < A[i]. Example: 5 has index 0 and 3 has index 2 now (5,3) pair is inversion as 0 < 2 and 5 > 3 which will satisfy out conditions and for reverse sorted array we will get maximum inversions and that is (n)*(n-1) / 2.For above given array there is 4 + 3 + 2 + 1 = 10 inversions.
"""

#Approaches:
"""
1.Brute-Force:
    # First, we will run a loop(say i) from 0 to N-1 to select the first element in the pair.
    # As index j should be greater than index i, inside loop i, we will run another loop i.e. j from i+1 to N-1.
    # Inside this second loop, we will check if a[i] > a[j] i.e. if a[i] and a[j] can be a pair. If they satisfy the condition, we will increase the count by 1.
    # Finally, we will return the count i.e. the number of such pairs.
    TC:O(n*2) SC:O(1)
2.Optimal Approach(Using Merge SOrt):
    # In the merge function, we will use a temp array to store the elements of the two sorted arrays after merging. Here, the range of the left array is low to mid and the range for the right half is mid+1 to high.
    # Now we will take two pointers left and right, where left starts from low and right starts from mid+1.
    # Using a while loop( while(left <= mid && right <= high)), we will select two elements, one from each half, and will consider the smallest one among the two. Then, we will insert the smallest element in the temp array. 
    # After that, the left-out elements in both halves will be copied as it is into the temp array.
    # Now, we will just transfer the elements of the temp array to the range low to high in the original array.
    
    # Modifications in merge() and mergeSort(): 
    # In order to count the number of pairs, we will keep a count variable, cnt, initialized to 0 beforehand inside the merge().
    # While comparing a[left] and a[right] in the 3rd step of merge(), if a[left] > a[right], we will simply add this line:
    # cnt += mid-left+1 (mid+1 = size of the left half)
    # Now, we will return this cnt from merge() to mergeSort(). 
    # Inside mergeSort(), we will keep another counter variable that will store the final answer. With this cnt, we will add the answer returned from mergeSort() of the left half, mergeSort() of the right half, and merge().
    # Finally, we will return this cnt, as our answer from mergeSort()

"""

from typing import *
import math
def merge(arr : List[int], low : int, mid : int, high : int) -> int:
    temp = []   # temporary array
    left = low  # starting index of left half of arr
    right = mid + 1 # starting index of right half of arr

    cnt = 0     # Modification 1: cnt variable to count the pairs

    # storing elements in the temporary array in a sorted manner
    while (left <= mid and right <= high):
        if (arr[left] <= arr[right]):
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            cnt += (mid - left + 1)  # Modification 2
            right += 1

    # if elements on the left half are still left
    while (left <= mid):
        temp.append(arr[left])
        left += 1

    # if elements on the right half are still left
    while (right <= high):
        temp.append(arr[right])
        right += 1

    # transfering all elements from temporary to arr
    for i in range(low, high + 1):
        arr[i] = temp[i - low]

    return cnt   # Modification 3

def mergeSort(arr : List[int], low : int, high : int) -> int:
    cnt = 0
    if low >= high:
        return cnt
    mid = math.floor((low + high) / 2)
    cnt += mergeSort(arr, low, mid)    # left half
    cnt += mergeSort(arr, mid + 1, high)  # right half
    cnt += merge(arr, low, mid, high)  # merging sorted halves
    return cnt

def numberOfInversions(a : List[int], n : int) -> int:
    # Write your code here.
    return mergeSort(a,0,n-1)
    pass