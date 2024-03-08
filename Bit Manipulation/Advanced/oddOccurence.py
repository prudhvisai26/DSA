"""
Problem statement
You are given an array 'arr' of size 'n'.
It contains an even number of occurrences for all numbers except two numbers.
Find those two numbers which have odd occurrences and return in decreasing order.

Sample Input 1:
4
3 3 1 2 
Sample Output 1:
2 1
Explanation of sample output 1:
'n' = 4, ‘arr’ = {3, 3, 1, 2}
Answer is {2, 1}
Here, numbers 1, 2 have occurrence 1 i.e. odd and number 3 have occurrence 2 i.e. even.
"""

def twoOddNum(arr : List[int]) -> List[int]:
    # Write your code here.
    xor2=arr[0]
    setbit=0
    n=len(arr)
    x,y=0,0
    
    for i in range(1,n):
        xor2=xor2^arr[i]
    setbit=xor2&~(xor2-1)
    
    for i in range(n):
        if arr[i]&setbit:
            x=x^arr[i]
        else:
            y=y^arr[i]
    if x>y:
        return x,y
    return (y,x)
