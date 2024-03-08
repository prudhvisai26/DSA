"""
Set The Rightmost Unset Bit

Problem statement
The problem is to find the rightmost bit of a non-negative number 'N' that is currently unset (i.e., has a value of 0) in its binary representation and set it to 1.
Return the number after setting the rightmost unset bit of 'N'. If there are no unset bits in N's binary representation, then the number should remain unchanged.

Sample Input 1:
10
Sample Output 1:
11
Explanation Of Sample Input 1:
N=10
The binary representation of 10 is 1010. After setting the rightmost unset bit it becomes 1011 which is 11.
"""

def setBits(N : int) -> int:
    # Write your code here.
    if ((N&(N+1))==0):
        return N
    return N|(N+1)
    pass
