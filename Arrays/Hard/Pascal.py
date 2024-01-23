# Program to generate Pascals Triangle
# Problem Statement: This problem has 3 variations. They are stated below:
"""
Example 1:
Input Format: N = 5, r = 5, c = 3
Result: 6 (for variation 1)
1 4 6 4 1 (for variation 2)

1 
1 1 
1 2 1 
1 3 3 1 
1 4 6 4 1    (for variation 3)

Explanation: There are 5 rows in the output matrix. Each row is formed using the logic of Pascal’s triangle.

Example 2:
Input Format: N = 1, r = 1, c = 1
Result: 1 (for variation 1)
    1 (for variation 2)
    1  (for variation 3)
Explanation: The output matrix has only 1 row.
"""

#Variation 1: Given row number r and column number c. Print the element at position (r, c) in Pascal’s triangle.:
"""
#Approaches:
    1.Brute Force:
        #Generate the Pascal triangle and find out the element at position (r,c)
        TC:O(n*3)//O(n*2) SC:O(r*c)
    2.Naive Approach: 
        #We can separately calculate n!, r!, (n-r)! and using their values we can calculate nCr. 
        #This is an extremely naive way to calculate. The time complexity will be O(n)+O(r)+O(n-r).
    3.Optimal Approach(nCr):
        # First, we will consider r-1 as n and c-1 as r.
        # After that, we will simply calculate the value of the combination using a loop. 
        # The loop will run from 0 to r. And in each iteration, we will multiply (n-i) with the result and divide the result by (i+1).
        # Finally, the calculated value of the combination will be our answer.
        TC:O(column) Sc:O(1)
"""
#Code:
def nCr(n,r):
    res=1
    for i in range(r):
        res=res*(n-i)
        res//=i+1
    print(res)
r = 6
c = 2
nCr(r-1,c-1)

#Variation 2: Given the row number n. Print the n-th row of Pascal’s triangle.

#Approach:
"""
1.Optimal Approach:
    # We will use a loop(say c) to iterate over each column i.e. from 1 to n. And for each column, we will do the following steps:
    # First, we will consider n-1 as n and c-1 as r.
    # After that, we will simply calculate the value of the combination using a loop. 
    # The loop will run from 0 to r. And in each iteration, we will multiply (n-i) with the result and divide the result by (i+1).
    # Finally, we will print the element.
    # Finally, the entire row will be printed.
    TC:O(r) SC:O(1)
"""
#Code:
def Generaterow(n):
    ans=1
    res=[ans]
    for i in range(1,n):
        ans=ans*(n-i)
        ans=ans//i
        res.append(ans)
        # print(ans,end=" ")
    return res
Generaterow(5)

#Variation 3: Given the number of rows n. Print the first n rows of Pascal’s triangle.
#Approach:
"""
1.Optimal Approach:
    #First, we will run a loop(say row) from 1 to n.
    # We will use a loop(say col) to iterate over each column i.e. from 1 to n. And inside the nested loops, we will do the following steps:
    # First, we will consider row-1 as n and col-1 as r.
    # After that, we will simply calculate the value of the combination using a loop. 
    # The loop will run from 0 to r. And in each iteration, we will multiply (n-i) with the result and divide the result by (i+1).
    # Finally, we will add the element to a temporary list.
    # After calculating all the elements for all columns of a row, we will add the temporary list to our final answer list.
    # Finally, we will return the answer list.
"""
def PascalTriangle(n):
    pascal=[]
    for i in range(1,n+1):
        pascal.append(Generaterow(i))
    return pascal
print(PascalTriangle(5))