"""
Problem statement
You are given a string ‘s’ of size ’n’, representing the prefix form of a valid mathematical expression.
Your task is to find out its corresponding postfix expression.
The expected time and space complexity is O(n) and O(n), where ‘n’ is the size of the string ‘s’.

Note:
The only operators used in the expressions are ‘+’, ‘-’, ‘*’, ‘/’.
Example:
Input: ‘n’ = 5, ‘s’ = “/A+BC”
Output: ABC+/
Explanation: For ‘s’ = “/A+BC”, the correct postfix expression is “ABC+/”.

"""
def preToPost(s: str) -> str:
    res=[]
    for i in range(len(s)-1,-1,-1):
        c=s[i]
        if c.isalpha() or c.isdigit():
            res.append(c)
        else:
            st=res.pop()+res.pop()+c
            res.append(st)
    return res.pop()
    pass
