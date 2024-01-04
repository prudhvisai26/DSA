"""
Check if a number is Armstrong Number or not
Problem Statement: Given a number, check if it is Armstrong Number or Not.

Examples:

Example 1:
Input:153 
Output: Yes, it is an Armstrong Number
Explanation: 1^3 + 5^3 + 3^3 = 153

Input:170 
Output: No, it is not an Armstrong Number
Explanation: 1^3 + 7^3 + 0^3 != 170
What are Armstrong Numbers?

Armstrong Numbers are the numbers having the sum of digits raised to power no. of digits is equal to a given number. Examples- 0, 1, 153, 370, 371, 407, and 1634 are some of the Armstrong Numbers.
"""

def ArmstrongNumber(n):
    c=Count_Digits(n)
    res=0
    t=n
    while(n>0):
        r=n%10
        res+=pow(r,c)
        n//=10
    return res==t

def Count_Digits(n):
    count=0
    while(n>0):
        count+=1
        n=n//10
    return count

print(ArmstrongNumber(153))