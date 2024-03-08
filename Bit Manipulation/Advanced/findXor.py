"""
Problem statement

You are given two numbers 'L' and 'R'.
Find the XOR of the elements in the range [L, R].

For Example:
For 'L' = 1 and ‘R’ = 5.
The answer is 1.

Sample Input 1:
3 5
Sample Output 1:
2
Explanation of sample output 1:
'L' = 3 and ‘R’ = 5
Answer is 2. Value of 3^4^5 is 2.
"""

def find(n):
    if n%4==0:
        return n
    elif n%4==1:
        return 1
    elif n%4==2:
        return n+1
    elif n%4==3:
        return 0
def findXOR(L : int, R : int) -> int:
    # Write your code here.
    ans=find(R)^find(L-1)
    return ans
    pass
