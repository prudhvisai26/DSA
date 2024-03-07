"""
Problem statement
You have been given an integer 'N'. Your task is to generate and return all binary strings of length 'N' such that there are no consecutive 1's in the string.

A binary string is that string which contains only ‘0’ and ‘1’.

For Example:
Let ‘N'=3, hence the length of the binary string would be 3. 

We can have the following binary strings with no consecutive 1s:
000 001 010 100 101 

Sample Input 1:
4
Sample Output 1:
0000 0001 0010 0100 0101 1000 1001 1010 
Explanation of sample input 1:
For N = 4 we get the following Strings:

0000 0001 0010 0100 0101 1000 1001 1010 

Note that none of the strings has consecutive 1s. Also, note that they are in a lexicographically increasing order.
"""

def generateString(N: int) -> List[str]:
    # write your code here
    ans=[]
    st=''
    generate(ans,st,N)
    return ans
def generate(ans,st,n):
    if n==0:
        ans.append(st) 
        return
    if(len(st)==0 or st[-1]=='0'):
        generate(ans,st+"0",n-1)
        generate(ans,st+"1",n-1)
    else:
        generate(ans,st+"0",n-1)
