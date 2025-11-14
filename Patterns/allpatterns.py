def pattern1():
    n,m=5,5
    for i in range(n):
        for j in range(m):
            print("*",end=" ")
        print()

def pattern2():
    m,n=5,5
    for i in range(1,m+1):
        for j in range(i):
            print("*",end=" ")
        print()

def pattern3():
    m,n=5,5
    for i in range(1,m+1):
        for j in range(i):
            print(j+1,end=" ")
        print()

def pattern4():
    m,n=5,5
    for i in range(1,m+1):
        for j in range(i):
            print(i,end=" ")
        print()

def pattern5():
    m,n=5,5
    for i in range(n,-1,-1):
        for j in range(i):
            print("*",end="")
        print()

def pattern6():
    m,n=5,5
    for i in range(n,-1,-1):
        for j in range(i):
            print(j+1,end="")
        print()

def pattern7():
    n=5
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
        for j in range(2*i+1):
            print("*",end="")
        for j in range(n-i-1):
            print(" ",end="")
        print()

def pattern8():
    n=5
    for i in range(n):
        for j in range(i):
            print(" ",end="")
        for j in range((2*(n-i))-1):
            print("*",end="")
        for j in range(i):
            print(" ",end="")
        print()

def pattern9():
    pattern7()
    pattern8()

def pattern10():
    n=5
    for i in range(1,(2*n-1)+1):
        stars=i
        if i>n:
            stars=2*n-i
        for j in range(1,stars+1):
            print("*",end="")
        print()

def pattern11():
    #flip
    n=5
    for i in range(1,n+1):
        if i%2==0:
            start=0
        else:
            start=1
        for j in range(1,i+1):
            print(start,end="")
            start=1-start
        print()

def pattern12():
    n=4
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end="")
        k=2*n-2*i
        for j in range(k):
            print(" ",end="")
        for j in range(i,0,-1):
            print(j,end="")
        print()

def pattern13():
    n=5
    st=1
    for i in range(n+1):
        for j in range(i):
            print(st,end=" ")
            st+=1
        print()

def pattern14():
    n=5
    for i in range(n+1):
        st=65
        for j in range(i):
            print(chr(st),end="")
            st+=1
        print()

def pattern15():
    n=5
    for i in range(n,-1,-1):
        st=65
        for j in range(i):
            print(chr(st),end="")
            st+=1
        print()

def pattern16():
    n=5
    st=65
    for i in range(1,n+1):
        for j in range(i):
            print(chr(st),end="")
        st+=1
        print()

def pattern17():
    n=5
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
        st="A"
        breakpoint=(2*i+1)//2
        for j in range(1,(2*i+1)+1):
            print(st,end="")
            if j>breakpoint:
                c=ord(st)-1
                st=chr(c)
            else:
                c=ord(st)+1
                st=chr(c)
        for j in range(n-i-1):
            print(" ",end="")
        print()

def pattern18():
    n=5
    for i in range(n):
        st=65+(n-i-1)
        for j in range(i+1):
            print(chr(st),end=" ")
            st+=1
        print()
        

# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# **********


def pattern19():
    n=5
    sp=0
    for i in range(n):
        for j in range(n-i):
            print("*",end="")
        for j in range(sp):
            print(" ",end="")
        for j in range(n-i):
            print("*",end="")
        sp+=2
        print()
    sp=2*(n-1)
    for i in range(n):
        for j in range(i+1):
            print("*",end="")
        for j in range(sp):
            print(" ",end="")
        for j in range(i+1):
            print("*",end="")
        print()
        sp-=2


# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *


def pattern20():
    n=5
    sp=2*(n-1)
    for i in range(n):
        for j in range(i+1):
            print("*",end="")
        for j in range(sp):
            print(" ",end="")
        for j in range(i+1):
            print("*",end="")
        print()
        sp-=2
    
    sp=2
    for i in range(n):
        if i==0:
            continue
        for j in range(n-i):
            print("*",end="")
        for j in range(sp):
            print(" ",end="")
        for j in range(n-i):
            print("*",end="")
        sp+=2
        print()


def pattern21():
    n=5
    for i in range(n):
        for j in range(n):
            if i==0 or j==0 or i==n-1 or j==n-1:
                print("*",end="")
            else:
                print(" ",end="")
        print()

def pattern22():
    n=4
    for i in range(2*n-1):
        for j in range(2*n-1):
            top=i
            left=j
            right=(2*n-2)-j
            bottom=(2*n-2)-i
            print(n-min(min(top,bottom),min(left,right)),end="")
        print()
