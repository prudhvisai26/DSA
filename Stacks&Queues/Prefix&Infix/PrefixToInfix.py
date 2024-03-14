"""
Problem statement
You are given a string denoting a valid Prefix expression containing ‘+’, ’-’, ’*’, ‘/’ and lowercase letters.

Convert the given Prefix expression into an Infix expression.

Note:
Infix notation is a method of writing mathematical expressions in which operators are placed between operands. For example, "a + b" represents the addition of a and b.
Prefix notation is a method of writing mathematical expressions in which operators are placed before the operands. For example, "+ a b" represents the addition of a and b.
Expression contains lowercase English letters, ‘+’, ‘-’, ‘*’, and  ‘/’. 

Example:
Input: /-ab+-cde
Output: ((a-b)/((c-d)+e))

Explanation:
In this test case, there are four operators ‘/’, ‘-’, ‘+’, ‘-’.
Prefix expression:  /-ab+-cde. 
The operator between  ‘a’ and ‘b’ is ‘-’. Resulting expression: /(a-b)+-cde.
The operator between  ‘c’ and ‘d’ is ‘-’. Resulting expression: /(a-b)+(c-d)e.
The operator between ‘c-d’ and ‘e’ is +. Resulting expression: /(a-b)((c-d)+e).
The operator between ‘a-b’ and ‘((c-d)+e)’ is ‘/’. Resulting expression: ((a-b)/((c-d)+e)).
"""

def prefixToInfixConversion(s: str) -> str:
  # Write your code here.
    stack=[]
    for i in range(len(s)-1,-1,-1):
        c=s[i]
        if c.isalpha() or c.isdigit():
            stack.append(c)
        else:
            res="("+stack.pop()+c+stack.pop()+")"
            stack.append(res)
    return stack.pop()
    pass
