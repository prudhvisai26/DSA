# Spiral Traversal of Matrix
# Problem Statement: Given a Matrix, print the given matrix in spiral order.

"""
Example 1:
Input: Matrix[][] = { { 1, 2, 3, 4 },
		      { 5, 6, 7, 8 },
		      { 9, 10, 11, 12 },
	              { 13, 14, 15, 16 } }

Outhput: 1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10.
Explanation: The output of matrix in spiral form.

Example 2:
Input: Matrix[][] = { { 1, 2, 3 },
	              { 4, 5, 6 },
		      { 7, 8, 9 } }
			    
Output: 1, 2, 3, 6, 9, 8, 7, 4, 5.
Explanation: The output of matrix in spiral form.
"""

#Approach:
"""
In this approach, we will be using four loops to print all four sides of the matrix.

1st loop: This will print the elements from left to right.
2nd loop: This will print the elements from top to bottom.
3rd loop: This will print the elements from right to left.
4th loop: This will print the elements from bottom to top.

Steps:
# Create and initialize variables top as starting row index, bottom as ending row index left as starting column index, and right as ending column index.
# In each outer loop traversal print the elements of a square in a clockwise manner.
# Print the top row, i.e. Print the elements of the top row from column index left to right and increase the count of the top so that it will move to the next row.
# Print the right column, i.e. Print the rightmost column from row index top to bottom and decrease the count of right.
# Print the bottom row, i.e. if top <= bottom, then print the elements of a bottom row from column right to left and decrease the count of bottom
# Print the left column, i.e. if left <= right, then print the elements of the left column from the bottom row to the top row and increase the count of left.
# Run a loop until all the squares of loops are printed.

# Note: As we can see in the code snippet below, two edge conditions are being added in the last two for loops: when we are moving from right to left and from bottom to top. 
These conditions are added to check if the matrix is a single column or a single row. So, whenever the elements in a single row are traversed they cannot be traversed again backward so the condition is checked in the right-to-left loop. When a single column is present, the condition is checked in the bottom-to-top loop as elements from bottom to top cannot be traversed again.
"""

def spiral(matrix):
    n=len(matrix)
    m=len(matrix[0])

    top,left=0,0
    bottom,right=n-1,m-1
    a=[]

    while(left<=right and top<=bottom):
        for i in range(left,right+1):
            a.append(matrix[top][i])
        top+=1
        for i in range(top,bottom+1):
            a.append(matrix[i][right])
        right-=1
        if(top<=bottom):
            for i in range(right,left-1,-1):
                a.append(matrix[bottom][i])
        bottom-=1
        if(left<=right):
            for i in range(bottom,top-1,-1):
                a.append(matrix[i][left])
        left+=1
    print(a)
spiral([[1,2,3],[4,5,6],[7,8,9]])