"""
Problem statement

Given an integer ‘N’, your task is to write a program that returns all the divisors of ‘N’ in ascending order.
For example:
'N' = 5.
The divisors of 5 are 1, 5.

Sample Input 1 :
10
Sample Output 1 :
1 2 5 10
Explanation of Sample Input 1:
The divisors of 10 are 1,2,5,10.
"""

def printDivisors(n: int) -> List[int]:
    # Write your code here
    xor=0
    f1=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            f1.append(i)
        if n//i!=i and n%(n//i)==0:
            f1.append(n//i)
    # print(f1)
    f1.sort()
    return f1
    pass
