"""
Input: N = 3
Output: 
* * *
* * *
* * *
"""
#Pattern-1 Code:
def pattern1(n):
    for i in range(n):
        for j in range(n):
            print('*',end=' ')
        print()

"""
Input:  n = 3
Output: 
* 
* *
* * *
"""

def pattern2(n):
    for i in range(n):
        for j in range(0,i+1):
            print("*",end=" ")
        print()


"""
Input: N = 3

Output: 
* * *
* *
*

"""
def pattern3(n):
    for i in range(n-1,-1,-1):
        for j in range(i+1):
            print("*",end=" ")
        print()

"""
Input: N = 3

Output: 

  *
 ***
*****

"""

def pattern4(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end='')
        for j in range(2*i+1):
            print("*",end='')
        for j in range(n-i-1):
            print(" ",end="")
        print()

"""
Input: N = 3

Output: 

*****
 ***
  *
"""

def pattern5(n):
    for i in range(n-1,-1,-1):
        for j in range(n-i-1):
            print(" ",end="")
        for j in range(2*i+1):
            print("*",end="")
        for j in range(n-i-1):
            print(" ",end='')
        print()

"""
Input: N = 3
Output: 
  *
 ***
*****
*****
 ***
  *

"""

def nStarDiamond(n):
    # Top part of diamond:
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
        for j in range(2*i+1):
            print("*",end="")
        for j in range(n-i-1):
            print(" ",end='')
        print()
    #Bottom part of Diamond:
    for i in range(n-1,-1,-1):
        for j in range(n-i-1):
            print(" ",end="")
        for j in range(2*i+1):
            print("*",end="")
        for j in range(n-i-1):
            print(" ",end='')
        print()


"""
Input: N = 3

Output: 
*
**
***
**
*
"""

def nStarTriangle(n):
    for i in range(2*n-1):
        if(i<n):
            for j in range(i+1):
                print("*",end="")
            for j in range(n-i-1):
                print(" ",end="")
        else:
            for j in range(2*n-i-1):
                print("*",end="")
            for j in range(n//2):
                print(" ",end="")
        print()