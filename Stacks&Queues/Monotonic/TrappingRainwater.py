"""
Problem statement
You have been given a long type array/list 'arr’ of size 'n’.
It represents an elevation map wherein 'arr[i]’ denotes the elevation of the 'ith' bar.
Print the total amount of rainwater that can be trapped in these elevations.

Note :
The width of each bar is the same and is equal to 1.

Sample Input 1:
4
2 1 1 4
Sample Output 1:
2
Explanation Of Sample Input 1:
Water trapped by:
     block of height 2 is 0 units.
     block of height 1 is 1 unit.
     block of height 1 is 3 1 unit. 
     block of height 4 is 3 0 units.

Hence the total is 2.
"""

def getTrappedWater(arr,n):
    # Write your code here.
    left,right=0,n-1
    leftmax,rightmax=0,0
    res=0
    while(left<=right):
        if arr[left]<=arr[right]:
            if arr[left]>=leftmax:
                leftmax=arr[left]
            else:
                res+=leftmax-arr[left]
            left+=1
        else:
            if arr[right]>=rightmax:
                rightmax=arr[right]
            else:
                res+=rightmax-arr[right]
            right-=1
    return res
