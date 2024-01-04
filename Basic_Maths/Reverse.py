"""
Example 1:
Input: N = 123
Output: 321
Explanation: The reverse of 123 is 321

"""
# Method 1: Using an integer
# TC->O(n) and SC->O(1)
def reverse(n):
    res=0
    while(n>0):
        r=n%10
        n=n//10
        res=(res*10)+r
    return res

#Method 2:Using Strings
# TC->O(n) and SC->O(1)
def reverse(n):
    res=''
    while(n>0):
        r=n%10
        n=n//10
        res+=str(r)
    return res