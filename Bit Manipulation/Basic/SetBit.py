"""
Check whether K-th bit is set or not

Problem statement
Given a number ‘N’ and a number ‘K’. Return true if ‘K’th bit of number is set, else return false.

Example:
Input: ‘N’ = 5, ‘K’ = 1
Output: YES
5 in binary can be written as 101 and as we can see a first bit from the right of 5 is set so the answer is 'YES'.

Sample Input 1 :
3 2
Sample Output 1 :
YES
Explanation Of Sample Input 1 :
3 in binary can be represented as 11 and 2 bit from right is set there, So answer is 'YES'.
"""

def isKthBitSet(n: int, k: int) -> bool:
    # Write your code from here.
    z=n&(2**(k-1))
    if z==0:
        return False
    return True
    pass
