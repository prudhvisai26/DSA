# Search in a sorted 2D matrix
# Problem Statement: You have been given a 2-D array ‘mat’ of size ‘N x M’ where ‘N’ and ‘M’ denote the number of rows and columns, respectively. 
# The elements of each row are sorted in non-decreasing order. Moreover, the first element of a row is greater than the last element of the previous row (if it exists). 
# You are given an integer ‘target’, and your task is to find if it exists in the given ‘mat’ or not.

"""
Example 1:
Input Format: N = 3, M = 4, target = 8,
mat[] = 
1 2 3 4
5 6 7 8 
9 10 11 12
Result: true
Explanation: The ‘target’  = 8 exists in the 'mat' at index (1, 3).

Example 2:
Input Format: N = 3, M = 3, target = 78,
mat[] = 
1 2 4
6 7 8 
9 10 34
Result: false
Explanation: The ‘target' = 78 does not exist in the 'mat'. Therefore in the output, we see 'false'.

"""

# Approach:
"""
Place the 2 pointers i.e. low and high: Initially, we will place the pointers. The pointer low will point to 0 and the high will point to (NxM)-1.
Calculate the ‘mid’: Now, inside the loop, we will calculate the value of ‘mid’ using the following formula:
mid = (low+high) // 2 ( ‘//’ refers to integer division)
Eliminate the halves based on the element at index mid: To get the element, we will convert index ‘mid’ to the corresponding cell using the above formula. Here no. of columns of the matrix = M.
row = mid / M, col = mid % M.
If matrix[row][col] == target: We should return true here, as we have found the ‘target’.
If matrix[row][col] < target: In this case, we need bigger elements. So, we will eliminate the left half and consider the right half (low = mid+1).
If matrix[row][col] > target: In this case, we need smaller elements. So, we will eliminate the right half and consider the left half (high = mid-1).
Steps 2-3 will be inside a while loop and the loop will end once low crosses high
(i.e. low > high). If we are out of the loop, we can say the target does not exist in the matrix. So, we will return false.
"""

def searchMatrix(mat,target):
    # Write your code here.
    n=len(mat)
    m=len(mat[0])
    low=0
    high=n*m-1
    while(low<=high):
        mid=(low+high)//2
        i=mid//m
        j=mid%m
        if mat[i][j]==target:
            return True
        elif mat[i][j]<target:
            low=mid+1
        else:
            high=mid-1
    return False