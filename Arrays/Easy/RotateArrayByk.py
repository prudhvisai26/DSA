#RotateArrayByk

#Problem Statement: Given an array of integers, rotating array of elements by k elements either left or right.
"""
Example 1:
Input: N = 7, array[] = {1,2,3,4,5,6,7} , k=2
Output: 6 7 1 2 3 4 5
Explanation: array is rotated to right by 2 position .

"""
#Approaches:

"""
1.BruteForce:
    #if k is greater than the size of array then update k=k%n.
    #Take a temp array of size k and store the last k elements in it.
    #Then copy the first n-k elements from original array to temp array.
    TC:O(n) SC:O(k)
2.Optimal (Reversing):
    #if k is greater than the size of array then update k=k%n.
    #First Reverse the last k elements of array i.e., (n-k,n-1)
    #Now Reverse the first n-k elements i.e., (0,n-k-1)
    #Finally reverse the Entire array. 
    TC:O(n) SC:O(n)
"""
def reverse(a,i,j):
    while(i<=j):
        t=a[i]
        a[i]=a[j]
        a[j]=t
        i+=1
        j-=1

def RotateArrayByk(a,k):
    n=len(a)
    k=k%n
    reverse(a,0,n-k-1)
    reverse(a,n-k,n-1)
    reverse(a,0,n-1)
    print(a)
RotateArrayByk([1,2,3,4,5,6,7],3)  