"""
Problem statement

You are given an integer 'N'.
You must return the unique prime factors of 'N' in increasing order.

For Example:
For ‘N’ = 10.
Unique prime factors are 2 and 5.
Hence we return {2, 5

Sample Input 1:
35
Sample Output 1:
5 7

Explanation For Sample Output 1:
Unique prime factors are 5 and 7.
Hence we return {5, 7}.
"""
def countPrimes(n: int) -> int:
    # Write your code here.
    s=[1]*(n+1)
    s[0]=0
    s[1]=0
    for i in range(2,n+1):
        if s[i]:
            j=i*i
            while j<=n:
                s[j]=0
                j=j+i
    ans=[]
    for i in range(2,n+1):
        if s[i] and n%i==0:
            ans.append(i)
    return ans
    pass
