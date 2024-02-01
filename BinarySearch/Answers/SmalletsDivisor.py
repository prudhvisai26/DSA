# Find the Smallest Divisor Given a Threshold
# Problem Statement: You are given an array of integers ‘arr’ and an integer i.e. a threshold value ‘limit’. Your task is to find the smallest positive integer divisor, such that upon dividing all the elements of the given array by it, the sum of the division’s result is less than or equal to the given threshold value.

"""
Example 1:
Input Format: N = 5, arr[] = {1,2,3,4,5}, limit = 8
Result: 3
Explanation: We can get a sum of 15(1 + 2 + 3 + 4 + 5) if we choose 1 as a divisor. 
The sum is 9(1 + 1 + 2 + 2 + 3)  if we choose 2 as a divisor. Upon dividing all the elements of the array by 3, we get 1,1,1,2,2 respectively. Now, their sum is equal to 7 <= 8 i.e. the threshold value. So, 3 is the minimum possible answer.

Example 2:
Input Format: N = 4, arr[] = {8,4,2,3}, limit = 10
Result: 2
Explanation: If we choose 1, we get 17 as the sum. If we choose 2, we get 9(4+2+1+2) <= 10 as the answer. So, 2 is the answer.

Point to remember:
While dividing the array elements with a chosen number, we will always take the ceiling value. And then we will consider their summation. For example, 3 / 2 = 2.

Observation: 
Minimum possible divisor: We can easily consider 1 as the minimum divisor as it is the smallest positive integer.
Maximum possible divisor: If we observe, we can conclude the maximum element in the array i.e. max(arr[]) is the maximum possible divisor. Any number > max(arr[]), will give the exact same result as max(arr[]) does. This divisor will generate the minimum possible result i.e. n(1 for each element), where n = size of the array.
With these observations, we can surely say that our answer will lie in the range 
[1, max(arr[])].

"""

import math
def Div(a,d):
    sum=0
    n=len(a)
    for i in range(n):
        sum+=math.ceil(a[i]/d)
    return sum

def smallestDivisor(arr,limit):
    # Write your code here.
    n=len(arr)
    low=1
    high,ans=max(arr),-1
    while(low<=high):
        mid=(low+high)//2
        if(Div(arr,mid)<=limit):
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans