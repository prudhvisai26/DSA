"""
Check if a number is Palindrome or Not
Problem Statement:  Given a number check if it is a palindrome.

**An integer is considered a palindrome when it reads the same backward as forward.**

Example 1:
Input: N = 123
Output: Not Palindrome Number
Explanation: 123 read backwards is 321.Since these are two different numbers 123 is not a palindrome.

Example 2:
Input: N =  121 
Output: Palindrome Number
Explanation: 121 read backwards as 121.Since these are two same numbers 121 is a palindrome.    

Approach:  We can reverse the original number and compare the original with the reversed number. If both are the same, the number qualifies as a palindrome number.

"""

def is_palindrome(n):
    if reverse(n)==n:
        return True
    else:
        return False
def reverse(n):
    res=0
    while(n>0):
        r=n%10
        n=n//10
        res=(res*10)+r
    return res
print("Enter a number to check if it's a palindrome or not")
if is_palindrome(121):
    print("Palindrome Number")
else:
    print("Not Palindrome Number")