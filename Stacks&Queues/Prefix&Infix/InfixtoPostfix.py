"""
Problem statement
You are given a string 'exp' which is a valid infix expression.
Convert the given infix expression to postfix expression.

Note:
Infix notation is a method of writing mathematical expressions in which operators are placed between operands. 
For example, "3 + 4" represents the addition of 3 and 4.
Postfix notation is a method of writing mathematical expressions in which operators are placed after the operands. 
For example, "3 4 +" represents the addition of 3 and 4.
Expression contains digits, lower case English letters, ‘(’, ‘)’, ‘+’, ‘-’, ‘*’, ‘/’, ‘^’. 

Example:
Input: exp = ‘3+4*8’
Output: 348*+

Explanation:
Here multiplication is performed first and then the addition operation. Hence postfix expression is  3 4 8 * +.
"""
def prec(s):
    if s=='+' or s=='-':
        return 1
    elif s=="*" or s=="/":
        return 2
    elif s=="^":
        return 3
    return -1
def infixToPostfix(exp: str) -> str:
    # Write your code here.
    s,res=[],""
    for i in range(len(exp)):
        c=exp[i]
        if c.isdigit() or c.isalpha():
            res+=c
        elif c=='(':
            s.append(c)
        elif c==')':
            while len(s)!=0 and s[-1]!='(':
                res+=s.pop()
            s.pop()
        else:
            while len(s)!=0 and prec(c)<=prec(s[-1]):
                res+=s.pop()
            s.append(c)
    while len(s)!=0:
        res+=s.pop()
    return res
