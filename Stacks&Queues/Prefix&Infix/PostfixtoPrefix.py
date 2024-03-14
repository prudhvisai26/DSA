"""
Problem statement
You are given a string denoting a valid Postfix expression containing ‘+’, ’-’, ’*’, ‘/’ and lowercase letters.
Convert the given Postfix expression into a Prefix expression.

Note:
Postfix notation is a method of writing mathematical expressions in which operators are placed after the operands. For example, "a b +" represents the addition of a and b.
Prefix notation is a method of writing mathematical expressions in which operators are placed before the operands. For example, "+ a b" represents the addition of a and b.
Expression contains lowercase English letters, ‘+’, ‘-’, ‘*’, and  ‘/’. 

Example:
Input: abc*+
Output: +a*bc

Explanation:
For the given postfix expression, infix expression is a+b*c. And it's corresponding prefix expression is +a*bc.
"""
def postfixToPrefix(s: str) -> str:
    # Write your code here.
    res=[]
    for i in range(len(s)):
        c=s[i]
        if c.isalpha() or c.isdigit():
            res.append(c)
        else:
            st=c+res.pop(-2)+res.pop()
            res.append(st)
    return res.pop()
    pass
