# Merge two Sorted Arrays Without Extra Space
# Problem statement: Given two sorted arrays arr1[] and arr2[] of sizes n and m in non-decreasing order. Merge them in sorted order. Modify arr1 so that it contains the first N elements and modify arr2 so that it contains the last M elements.

"""
Example 1:
Input: 
n = 4, arr1[] = [1 4 8 10] 
m = 5, arr2[] = [2 3 9]
Output: 
arr1[] = [1 2 3 4]
arr2[] = [8 9 10]
Explanation:
After merging the two non-decreasing arrays, we get, 1,2,3,4,8,9,10.
"""

#Approaches:
"""
1.Brute-Force:
    # We will first declare a third array, arr3[] of size n+m, and two pointers i.e. left and right, one pointing to the first index of arr1[] and the other pointing to the first index of arr2[].
    # The two pointers will move like the following:
    # If arr1[left] < arr2[right]: We will insert the element arr1[left] into the array and increase the left pointer by 1.
    # If arr2[right] < arr1[left]: We will insert the element arr2[right] into the array and increase the right pointer by 1.
    # If arr1[left] == arr2[right]: Insert any of the elements and increase that particular pointer by 1.
    # If one of the pointers reaches the end, then we will only move the other pointer and insert the rest of the elements of that particular array into the third array i.e. arr3[].
    # If we move the pointer like the above, we will get the third array in the sorted order.
    # Now, from sorted array arr3[], we will copy first n(size of arr1[]) elements to arr1[], and the next m(size of arr2[]) elements to arr2[].
    TC:O(n+m)+O(n+m) SC:O(n+m)
2.Optimal Approach 1:
    # We will declare two pointers i.e. left and right. The left pointer will point to the last index of the arr1[](i.e. Basically the maximum element of the array). The right pointer will point to the first index of the arr2[](i.e. Basically the minimum element of the array).
    # Now, the left pointer will move toward index 0 and the right pointer will move towards the index m-1. While moving the two pointers we will face 2 different cases like the following:
    # If arr1[left] > arr2[right]: In this case, we will swap the elements and move the pointers to the next positions.
    # If arr1[left] <= arr2[right]: In this case, we will stop moving the pointers as arr1[] and arr2[] are containing correct elements.
    # Thus, after step 2, arr1[] will contain all smaller elements and arr2[] will contain all bigger elements. Finally, we will sort the two arrays.
    TC:O(min(n,m))+O(n*logn)+O(m*logm) SC:O(1)
3.Optimal Approach (gap Method):
    # First, assume the two arrays as a single array and calculate the gap value i.e. ceil((size of arr1[] + size of arr2[]) / 2).
    # We will perform the following operations for each gap until the value of the gap becomes 0:
    # Place two pointers in their correct position like the left pointer at index 0 and the right pointer at index (left+gap).
    # Again we will run a loop until the right pointer reaches the end i.e. (n+m). Inside the loop, there will be 3 different cases:
    # If the left pointer is inside arr1[] and the right pointer is in arr2[]: We will compare arr1[left] and arr2[right-n] and swap them if arr1[left] > arr2[right-n].
    # If both the pointers are in arr2[]: We will compare arr1[left-n] and arr2[right-n] and swap them if arr1[left-n] > arr2[right-n].
    # If both the pointers are in arr1[]: We will compare arr1[left] and arr2[right] and swap them if arr1[left] > arr2[right].
    # After the right pointer reaches the end, we will decrease the value of the gap and it will become ceil(current gap / 2). 
    # Finally, after performing all the operations, we will get the merged sorted array.
    TC:O((n+m)*log(n+m)) Sc:O(1)
"""

# Optimal Approach -1:
def merge_sorted_arrays(a, n, b, m):
    left,right=n-1,0
    while(left>=0 and right<m):
        if a[left]>b[right]:
            a[left],b[right]=b[right],a[left]
            left-=1
            right+=1
        else:
            break
    a.sort()
    b.sort()
    print(a,b)
merge_sorted_arrays([1,4,8,10],4,[2 ,3, 9],3)

#Gap Method:
def swapIfGreater(a, b, ind1, ind2):
    if a[ind1] > b[ind2]:
        a[ind1], b[ind2] = b[ind2], a[ind1]
def gapMethod(a,b,n,m):
    len=n+m
    gap=(len//2)+(len%2)
    while(gap>0):
        left=0
        right=left+gap
        while(right<len):
            if(left<n and right>=n):
                swapIfGreater(a,b,left,right-n)
            elif(left>=n):
                swapIfGreater(b,b,left-n,right-n)
            else:
                swapIfGreater(a,a,left,right)
            left+=1
            right+=1
        if gap==1:
            break
        gap=(gap//2)+(gap)%2
    print(a,b)
gapMethod([1,4,8,10],[2 ,3, 9],4,3)