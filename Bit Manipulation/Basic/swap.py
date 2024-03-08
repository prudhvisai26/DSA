"""
Problem statement
You are given two numbers 'a' and 'b' as input.
You must swap the values of 'a' and 'b'.

Sample Input 1:
1 2 
Sample Output 1:
2 1
"""
def swapNumber(a:list,  b: list) -> None:
    # write your code here
    a[0]=a[0]^b[0]
    b[0]=a[0]^b[0]
    a[0]=a[0]^b[0]
    return a,b
