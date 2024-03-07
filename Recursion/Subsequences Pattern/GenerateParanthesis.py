"""
Problem statement
You are given an integer 'N', your task is to generate all combinations of well-formed parenthesis having ‘N’ pairs.
A parenthesis is called well-formed if it is balanced i.e. each left parenthesis has a matching right parenthesis and the matched pairs are well nested.

For Example:
For ‘N’ = 3,
All possible combinations are: 
((()))
(()())
(())()
()(())
()()()

Sample Input 1:
2
Sample Output 1:
()()
(())
Explanation For Sample Output 1:
There are two possible combinations of parentheses:
()()
(())
Here both the parenthesis are balanced so the possible outputs can be [ [ ()() ],[ (()) ] ].
Sample Input 2:
4
Sample Output 2:
()()()()
()()(())
()(())()
()(()())
()((()))
(())()()
(())(())
(()())()
(()()())
(()(()))
((()))()
((())())
((()()))
(((())))
"""
#Code:
def validParenthesis(n: int) -> int:
    # Write your code here.
    ans=[]
    s=''
    generate(n,0,0,s,ans)
    return ans
def generate(n,left,right,s,ans):
    if(len(s)==2*n):
        ans.append(s)
        return
    if left<n:
        generate(n,left+1,right,s+'(',ans)
    if right<left:
        generate(n,left,right+1,s+')',ans)
