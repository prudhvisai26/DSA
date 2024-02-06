# Remove Outermost Parentheses
# A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

# For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
# A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.
# Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.
# Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.


"""
Example 1:

Input: s = "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
Example 2:

Input: s = "(()())(())(()(()))"
Output: "()()()()(())"
Explanation: 
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
Example 3:

Input: s = "()()"
Output: ""
Explanation: 
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".
"""

#Approach:
"""
1.Initialize an empty String and count to 0 and Run a loop till len(s).
2.Now Add below conditions:
    #If the current character is '(' and count is zero increment it by 1 and if count>0 then store the current character in res string and increment count by 1.
    #If the current character is ')' and count is one decrement it by 1 and if count>1 then store the current character in res string and decrement coount by 1.
3.return result.
TC:O(len(s)) SC:O(1)
"""

# Code:
def removeOuterParentheses(s):
    res=''
    count=0
    for i in s:
        if i=='(' and count==0:
            count+=1
        elif i=='(' and count>0:
            res+=i
            count+=1
        elif i==')' and count>1:
            res+=i
            count-=1
        elif i==')' and count==1:
            count-=1
    return res