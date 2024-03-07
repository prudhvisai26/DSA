"""
Given a string 'S' of length 'N', return all the subsequences of the given string.
A subsequence is a sequence that can be derived from the given sequence by deleting zero or more elements without changing the order of the remaining elements.

Note :
You may return the subsequences in any order but they will be printed in lexicographically ascending order.

If a string from the returned array has a length of zero, it will be represented as 'Empty String' in the output.
For Example:
For a given word “cn” the possible subsequences are 'Empty String', 'c', 'cn' and 'n'.

We get :
'Empty String' by deleting 'c' and 'n'.
'c' by deleting 'n'.
'n' by deleting 'c'.
'cn' if we don't delete any thing.

Sample Input 1:
abc
Sample Output 1:
'Empty String'
a
ab
abc
ac
b
bc
c


Maintain a temp string (say f),which is empty initally.
Now you have two options,either you can pick the character or not pick the character and move to the next index.
Firstly we pick the character at ith index and then move to the next index.(f + s[i])
If the base condition is hit,i.e i==s.length() ,then we print the temp string and return.
Now while backtracking we have to pop the last character since now we have to implement the non-pick condition and then move to next index.
"""

def generateSubsequences(s:str) -> List[str]:
    # Write your code here.
    ans=[]
    solve(0,s,ans,'')
    return ans
def solve(i,s,ans,f):
    if(i==len(s)):
        ans.append(f)
        return
    solve(i+1,s,ans,f+s[i])
    solve(i+1,s,ans,f)
    pass
