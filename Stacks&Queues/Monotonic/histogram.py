"""
Problem statement
You have been given an array/list 'HEIGHTS' of length ‘N. 'HEIGHTS' represents the histogram and each element of 'HEIGHTS' represents the height of the histogram bar. 
Consider that the width of each histogram is 1.
You are supposed to return the area of the largest rectangle possible in the given histogram.

Sample Input 1 :
2
10
1 0 1 2 2 2 2 1 0 2 
10
1 2 1 0 1 1 0 0 2 2 
Sample Output 1 :
8
4
Explanation For Sample Input 1 :
In the first test case, the area of the largest rectangle of the given histogram is 8 in the rectangle starting from index 4 to index 7 in the given array/list.
In the second test case, the area of the largest rectangle of the given histogram is 4 in the rectangle starting from index 9 to index 10 in the given array/list.

"""

def largestRectangle(arr):
    # Write your code here.
    st=[]
    maxi=0
    n=len(arr)
    for i in range(0,n+1):
        while st and (i==n or arr[st[-1]]>=arr[i]):
            height=arr[st[-1]]
            st.pop()
            if len(st)==0:
                width=i
            else:
                width=i-st[-1]-1
            maxi=max(maxi,height*width)
        st.append(i)
    return maxi
    pass
