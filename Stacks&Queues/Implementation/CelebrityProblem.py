"""
Problem statement
There are ‘N’ people at a party. Each person has been assigned a unique id between 0 to 'N' - 1(both inclusive). A celebrity is a person who is known to everyone but does not know anyone at the party.

Given a helper function ‘knows(A, B)’, It will returns "true" if the person having id ‘A’ know the person having id ‘B’ in the party, "false" otherwise. Your task is to find out the celebrity at the party. Print the id of the celebrity, if there is no celebrity at the party then print -1.

Note:
1. The helper function ‘knows’ is already implemented for you.
2. ‘knows(A, B)’ returns "false", if A doesn't know B.
3. You should not implement helper function ‘knows’, or speculate about its implementation.
4. You should minimize the number of calls to function ‘knows(A, B)’.
5. There are at least 2 people at the party.
6. At most one celebrity will exist.

Sample Input 1:
1
2
Call function ‘knows(0, 1)’ // returns false
Call function ‘knows(1, 0)’ // returns true
Sample Output 1:
0
Explanation For Sample Input 1:
In the first test case, there are 2 people at the party. When we call function knows(0,1), it returns false. That means the person having id ‘0’ does not know a person having id ‘1'. Similarly, the person having id ‘1’  knows a person having id ‘0’ as knows(1,0) returns true. Thus a person having id ‘0’ is a celebrity because he is known to everyone at the party but doesn't know anyone.
Sample Input 2:
1
2
Call ‘knows(0, 1)’ // returns true
Call ‘knows(1, 0)’ // returns true
2
Call ‘knows(0, 1)’ // returns false
Call ‘knows(1, 0)’ // returns false
Sample Output 2:
-1
-1
Explanation For Sample Input 2:
In first test case, there are 2 people at the party. The person having id ‘0’  knows a person having id ‘1’. The person having id ‘1’  knows a person having id ‘0’. Thus there is no celebrity at the party, because both know each other. 
In second test case, there are 2 people at the party. The person having id ‘0’ does not knows a person having id ‘1’. The person having id ‘1’  also does not knows a person having id ‘0’. Thus there is no celebrity at the party, because both does not know each other. 

"""
from os import *
from sys import *
from collections import *
from math import *

'''
    This is signature of helper function 'knows'.
    You should not implement it, or speculate about its implementation.

    def knows(int A, int B); 
    Function 'knows(A, B)' will returns "true" if the person having
    id 'A' knows the person having id 'B' in the party, "false" otherwise.
'''

def findCelebrity(n, knows):

    # Write your code here.    
    s=[]
    for i in range(n):
        s.append(i)
    while len(s)>1:
        a=s.pop()
        b=s.pop()
        if(knows(a,b)):
            s.append(b)
        else:
            if knows(b,a):
                s.append(a)
    if len(s)==0:
        return -1
    g=s.pop()
    for i in range(n):
        if i!=g:
            if knows(i,g)==False or knows(g,i):
                return -1
    return g
    pass
