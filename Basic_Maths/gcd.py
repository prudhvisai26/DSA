"""
Find GCD of two numbers
Problem Statement: Find the gcd of two numbers.

Examples
Example 1:
Input: num1 = 4, num2 = 8
Output: 4
Explanation: Since 4 is the greatest number which divides both num1 and num2.

Example 2:
Input: num1 = 3, num2 = 6
Output: 3
Explanation: Since 3 is the greatest number which divides both num1 and num2.

"""

#Solution 1: Brute force
"""
Intuition: Simply traverse from 1 to min(a,b) and check for every number.
Approach: 

Traverse from 1 to min(a,b).
And check if i is divisible by both a and b.If yes store it in the answer.
Find the maximum value of i which divides both a and b.
"""
def gcd_bruteforce(num1, num2):
    ans=1
    for i in range(1,min(num1,num2)+1):
        if num1%i==0 and num2%i==0:
            ans=i
    return ans

"""
Solution 2: Using Euclidean’s theorem.
Intuition: Gcd is the greatest number which is divided by both a and b.If a number is divided by both a and b, it is should be divided by (a-b) and b as well.

Approach:
Recursively call gcd(b,a%b) function till the base condition is hit.
b==0 is the base condition.When base condition is hit return a,as gcd(a,0) is equal to a.

"""
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)