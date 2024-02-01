# Search in a row and column-wise sorted matrix
# Problem Statement: You have been given a 2-D array ‘mat’ of size ‘N x M’ where ‘N’ and ‘M’ denote the number of rows and columns, respectively. 
# The elements of each row and each column are sorted in non-decreasing order.
# But, the first element of a row is not necessarily greater than the last element of the previous row (if it exists).
# You are given an integer ‘target’, and your task is to find if it exists in the given ‘mat’ or not.

# Algorithm:
# As we are starting from the cell (0, m-1), the two variables i.e. ‘row’ and ‘col’ will point to 0 and m-1 respectively.
# We will do the following steps until row < n and col >= 0(i.e. while(row < n && col >= 0)):
# If matrix[row][col] == target: We have found the target and so we will return true.
# If matrix[row][col] > target: We need the smaller elements to reach the target. But the column is in increasing order and so it contains only greater elements. So, we will eliminate the column by decreasing the current column value by 1(i.e. col–) and thus we will move row-wise.
# If matrix[row][col] < target: In this case, We need the bigger elements to reach the target. But the row is in decreasing order and so it contains only smaller elements. So, we will eliminate the row by increasing the current row value by 1(i.e. row++) and thus we will move column-wise.
# If we are outside the loop without getting any matching element, we will return false.

#Incerasing and Decreasing:......


def searchElement(matrix,target):
    # Write your code here.
    n=len(matrix)
    m=len(matrix[0])
    r=0
    c=m-1
    while(r<n and c>=0):
        if matrix[r][c]==target:
            return 1
        elif matrix[r][c]<target:
            r+=1
        else:
            c-=1
    return 0