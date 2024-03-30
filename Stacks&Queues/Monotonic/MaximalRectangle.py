"""
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.

Example 2:
Input: matrix = [["0"]]
Output: 0

Example 3:
Input: matrix = [["1"]]
Output: 1

--Step 1: The largestRectangleArea Function
First, let's take a look at the largestRectangleArea function.The idea is to use a stack to efficiently find the maximum area.
Here's a simplified overview of the algorithm:
-Create an empty stack to store indices.
-Iterate through the histogram from left to right.
-While the stack is not empty and the current histogram value is less than the value at the index stored in the stack's top element, pop elements from the stack and calculate the maximum area for each popped element.
-Keep track of the maximum area as you iterate through the histogram.
-This algorithm efficiently finds the largest rectangle area in the histogram, which we'll use in the next step.

--Step 2: The maximalAreaOfSubMatrixOfAll1 Function
In this step, we adapt the largestRectangleArea function to solve the Maximal Rectangle Problem for a binary matrix. We create a vector to store the height of each column and use dynamic programming to find the maximum rectangle area for each row.

Dry Run of maximalRectangle Function
We'll perform a dry run of the maximalRectangle function using the following matrix:
matrix = [
    ['1', '0', '1', '0', '0'],
    ['1', '0', '1', '1', '1'],
    ['1', '1', '1', '1', '1'],
    ['1', '0', '0', '1', '0']
]

#Step 1: Initializing Variables
We start with the given matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
We have two helper functions, largestRectangleArea and maximalAreaOfSubMatrixOfAll1, which are used within the maximalRectangle function.

**Step 2: maximalAreaOfSubMatrixOfAll1
We enter the maximalAreaOfSubMatrixOfAll1 function, which computes the maximal area of submatrices containing only '1's.
Matrix and height after each row iteration:

Process Row 1:
Matrix:
1 0 1 0 0
Height: [1, 0, 1, 0, 0]

Process Row 2:
Matrix:
1 0 1 1 1
Height: [2, 0, 2, 1, 1]

Process Row 3:
Matrix:
1 1 1 1 1
Height: [3, 1, 3, 2, 2]

Process Row 4:
Matrix:
1 0 0 1 0
Height: [4, 1, 1, 3, 1]

Maximal Area of Histogram (largestRectangleArea):

For each height, we calculate the maximal area of the histogram using the largestRectangleArea function.

For the height [1, 0, 1, 0, 0], the maximal area is 1.
For the height [2, 0, 2, 1, 1], the maximal area is 4.
For the height [3, 1, 3, 2, 2], the maximal area is 6.
For the height [4, 1, 1, 3, 1], the maximal area is 4.
The maximal area of submatrices for each row is [1, 4, 6, 4].

Step 3: maximalRectangle
Finally, we return the maximum value from the array [1, 4, 6, 4], which is 6.
The maximal area of a submatrix containing only '1's in the given matrix is 6.
"""

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def largestRectangleArea(heights):
            s= []
            max_area = 0
            n = len(heights)
            for i in range(n + 1):
                while s and (i == n or heights[s[-1]] >= heights[i]):
                    height = heights[s.pop()]
                    width = i if not s else i - s[-1] - 1
                    max_area = max(max_area, height * width)
                s.append(i)
            return max_area
        def maximalAreaOfSubMatrixOfAll(mat, n, m):
            max_area = 0
            height = [0] * m
            for i in range(n):
                for j in range(m):
                    if mat[i][j] == '1':
                        height[j] += 1
                    else:
                        height[j] = 0

                area =largestRectangleArea(height)
                max_area = max(max_area, area)
            
            return max_area
        if not matrix:
            return 0
        n,m=len(matrix),len(matrix[0])
        return maximalAreaOfSubMatrixOfAll(matrix,n,m)
