"""
Problem statement
You're given a string 'S' consisting of "{", "}", "(", ")", "[" and "]" .
Return true if the given string 'S' is balanced, else return false.

For example:
'S' = "{}()".
There is always an opening brace before a closing brace i.e. '{' before '}', '(' before ').
So the 'S' is Balanced.

Sample Input 1 :
[()]{}{[()()]()}
Sample Output 1 :
Balanced
Explanation Of the Sample Input 1 :
There is always an opening brace before a closing brace i.e. '{' before '}', '(' before '), '[' before ']'.
So the 'S' is Balanced.
Sample Input 2 :
[[}[
Sample Output 2 :
Not Balanced
"""

def isValidParenthesis(s: str) -> bool:
    # Write your code here
    stack=[]
    for i in s:
        if i=='(' or i=='{' or i=='[':
            stack.append(i)
        else:
            if not stack:
                return False
            x=stack.pop()
            if x=='(' and i!=')':
                return False
            elif x=='[' and i!=']':
                return False
            elif x=='{' and i!='}':
                return False
    if stack:
        return False
    return True 


