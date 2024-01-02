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
1 2 
1 2 3

"""