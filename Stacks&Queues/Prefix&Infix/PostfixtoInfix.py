"""
Problem statement
You are given a mathematical expression in postfix notation. The expression consists of alphabets(both lowercase and uppercase) and operators.
Convert this expression to infix notation.

Note:
Surround every expression with a pair of parentheses “()”.

Example:
Input: ‘postfix’ = “ab+c+”
Output: ‘infix’ = “((a+b)+c)”
Explanation: The expression ((a+b)+c)” in infix is equivalent to “ab+c+” in postfix.

"""

def postToInfix(postfix: str) -> str:
    # Write your code here.
    st=[]
    for i in range(len(postfix)):
        c=postfix[i]
        if c.isalpha():
            st.append(c)
        else:
            res='('+st.pop(-2)+c+st.pop()+')'
            st.append(res)
    return st.pop()
    pass
