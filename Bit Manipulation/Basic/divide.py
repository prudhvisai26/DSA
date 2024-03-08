"""
# Divide Two Integers

Problem statement:

You are given two integers, ‘dividend’ and ‘divisor’.
You are required to divide the integers without using multiplication, division, and modular operators.
Your task is to return the quotient after dividing ‘dividend’ by ‘divisor’.

Note :
In cases where the dividend is not perfectly divisible by the divisor, you are required to return the integer value of the quotient which is closer to zero.
For example - If the answer is '8.34', we return the integer part, i.e., '8'. Also, If the answer is '-2.67', we return the integer part, i.e., '-2'.
Assume we're dealing with a system that can only store integers in the 32-bit signed integer range: [2^31, 2^31-1]. If the quotient is higher than 2^31 - 1, return 2^31 - 1; if it is less than -2^31, return -2^31. 
For example :
If the answer is ‘9.333’, then return ‘9’, or if the answer is ‘-8.123’, then return ‘-8’
"""

def divideTwoInteger(dividend: int, divisor: int) -> int:
    # write your code here
    sign=1
    q=0
    if dividend<0:
        sign=-1
    if divisor<0:
        sign*=-1
    dividend=abs(dividend)
    divisor=abs(divisor)
    while dividend>=divisor:
        dividend-=divisor
        q+=1
    return sign*q
