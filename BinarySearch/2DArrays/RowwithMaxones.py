# Find the row with maximum number of 1’s
# Problem Statement: You have been given a non-empty grid ‘mat’ with ‘n’ rows and ‘m’ columns consisting of only 0s and 1s. All the rows are sorted in ascending order.
# Your task is to find the index of the row with the maximum number of ones.
# Note: If two rows have the same number of ones, consider the one with a smaller index. If there’s no row with at least 1 zero, return -1.

"""
Example 1:
Input Format: n = 3, m = 3, 
mat[] = 
1 1 1
0 0 1
0 0 0
Result: 0
Explanation: The row with the maximum number of ones is 0 (0 - indexed).

Example 2:
Input Format: n = 2, m = 2 , 
mat[] = 
0 0
0 0
Result: -1
Explanation:  The matrix does not contain any 1. So, -1 is the answer.
"""

# Approach:
"""
First, we will declare 2 variables i.e. cnt_max(initialized with 0), and index(initialized with -1). The first variable will store the maximum number of 1’s we have got and ‘index’ will store the row number.
Next, we will start traversing the rows. We will use a loop(say i) to select each row at a time.
Now, for each row i, we will use lowerBound() to get the first occurrence of 1. Now, using the following formula we will calculate the number of 1’s:
Number_of_ones = m(number of columns) – lowerBound(1)(0-based index).
After that, we will compare it with cnt_max and if the current number of 1’s is greater, we will update cnt_max with the current no. of 1’s and ‘index’ with the current row index.
Finally, we will return the variable ‘index’. It will store the index of the row with the maximum no. of 1’s. And if the matrix does not contain any 1, it stores -1.
"""

def bs(a,n,x):
    low,high=0,n-1
    ans=n
    while(low<=high):
        mid=(low+high)//2
        if a[mid]>=x:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans

def rowWithMax1s(matrix: [[int]], n: int, m: int) -> int:
    maxi=0
    index=-1
    for i in range(n):
        cnt=m-bs(matrix[i],m,1)
        if cnt>maxi:
            maxi=cnt
            index=i
    return index