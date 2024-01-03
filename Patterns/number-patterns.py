"""
Input: N = 3
Output: 
1
1 2 
1 2 3

"""
def nTriangle(n):
    for i in range(n):
        for j in range(i+1):
            print(j+1,end=" ")
        print()
    pass

"""
Input: N = 3
Output: 
1
2 2 
3 3 3

"""
def triangle(n):
    for i in range(n):
        for j in range(i+1):
            print(i+1,end=' ')
        print()

"""
Input: N = 3
Output:
1 2 3
1 2
1

"""
def nNumberTriangle(n: int) -> None:
    # Write your solution here.
    for i in range(n-1,-1,-1):
        for j in range(i+1):
            print(j+1,end=" ")
        print()


"""
Input: N = 3
Output:
1
0 1
1 0 1

"""

def nBinaryTriangle(n):
    # Write your solution here.
    for i in range(n):
        s=0
        if((i+1)%2!=0):
            s=1
        for j in range(i+1):
            print(s,end=" ")
            s=1-s
        print()


"""
Input: N = 3
Output: 

1         1
1 2     2 1
1 2 3 3 2 1
"""

def numberCrown(n: int) -> None:
    # Write your solution here.
    s=2*(n-1)
    for i in range(n):
        for j in range(i+1):
            print(j+1,end=" ")
        for j in range(i,s):
            print(end=" ")
        for j in range(i+1,0,-1):
            print(j,end=" ")
        print()
        s-=2

"""
Input: N = 3
1
0 1
1 0 1

"""
def nNumberTriangle(n: int) -> None:
    # Write your solution here.
    s=1
    for i in range(n):
        for j in range(i+1):
            print(s,end=" ")
            s+=1
        print()



