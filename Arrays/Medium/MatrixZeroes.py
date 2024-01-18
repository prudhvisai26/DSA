# Set Matrix Zero
# Problem Statement: Given a matrix if an element in the matrix is 0 then you will have to set its entire column and row to 0 and then return the matrix.

"""
Examples 1:
Input: matrix=[[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Explanation: Since matrix[2][2]=0.Therfore the 2nd column and 2nd row wil be set to 0.
 
Input: matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output:[[0,0,0,0],[0,4,5,0],[0,3,1,0]]
Explanation:Since matrix[0][0]=0 and matrix[0][3]=0. Therefore 1st row, 1st column and 4th column will be set to 0
"""

#Approaches:
"""
1.Brute Force:
    #Run through 2 nested loops and check whether there is a zero or not
    #If a zero encountered uodate the respective row and column with -1
    #Finally update all elements which are marked as -1 to 0
    Time Complexity:O(n*m)*O(n+m) where O(n+m) is used to mark the rows and columns SC:O(1)
2.Approach 1:
    #Lets have 2 arrays with sizes of n and m and declare it with 0s
    #Now run through the given matrix and mark respective col and row array to 1 if any 0 appears in the matrix array.
    #Now run nested loop and just check whether if row or column is checked or 1 if it is then make the particular to 0.
    TC:O(n*m)+O(n*m) Sc:O(n)+O(m)
3.Optimal:
    #In this approach we try to reduce the SC from the above approach by directly accessing the first row and column in the matrix.
    #Firstly we run through the nested loop and find out whether the element is zero or not if it is make particular row and column 0.
    #Intitialize a var called col0 to 1 and update col0 only if the col==0 and matrix[0][0]=0
    #Now run the nested loop from 1 to n and check if the correspondinf row or column is 0 or not if it is then update the curr value to 0.
    #Finally update the first row and column by checking if mat[0][0]==0 and col==0
    TC:O(n*m)+O(n*m) Sc:O(1)
"""
def setZeroes(matrix):
    n=len(matrix)
    m=len(matrix[0])
    col0=1
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==0:
                matrix[i][0]=0
                if j!=0:
                    matrix[0][j]=0
                else:
                    col0=0
    for i in range(1,n):
        for j in range(1,m):
            if matrix[i][j]!=0:
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
    if matrix[0][0]==0:
        for i in range(m):
            matrix[0][i]=0
    if col0==0:
        for i in range(n):
            matrix[i][0]=0

    print(matrix)
setZeroes([[1,1,1,1],[1,0,1,1],[1,1,0,1],[1,0,0,1]])