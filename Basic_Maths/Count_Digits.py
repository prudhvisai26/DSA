#Method 1: 
# TC->O(n) and SC->O(1)

def countDigits(n: int) -> int:
    c=0
    while(n>0):
        c+=1
        n=n//10
    return c

#Method 2: 
# TC->O(n) and SC->O(1)

def countDigits(n: int) -> int:
    n=str(n)
    return len(n)


#Method 3: 
# TC->O(logn) and SC->O(1)
import math
def countDigits(n: int) -> int:
    # Write your code here
    return math.floor(math.log10(n)+1)