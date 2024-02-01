# Median of Two Sorted Arrays of different sizes
# Problem Statement: Given two sorted arrays arr1 and arr2 of size m and n respectively, return the median of the two sorted arrays. The median is defined as the middle value of a sorted list of numbers. In case the length of the list is even, the median is the average of the two middle elements.

"""
Example 1:
Input Format: n1 = 3, arr1[] = {2,4,6}, n2 = 3, arr2[] = {1,3,5}
Result: 3.5
Explanation: The array after merging 'a' and 'b' will be { 1, 2, 3, 4, 5, 6 }. As the length of the merged list is even, the median is the average of the two middle elements. Here two medians are 3 and 4. So the median will be the average of 3 and 4, which is 3.5.

Example 2:
Input Format: n1 = 3, arr1[] = {2,4,6}, n2 = 2, arr2[] = {1,3}
Result: 3
Explanation: The array after merging 'a' and 'b' will be { 1, 2, 3, 4, 6 }. The median is simply 3.
"""

#Approach:
"""
First, we have to make sure that the arr1[] is the smaller array. If not by default, we will just swap the arrays. Our main goal is to consider the smaller array as arr1[].
Calculate the length of the left half: left = (n1+n2+1) / 2.
Place the 2 pointers i.e. low and high: Initially, we will place the pointers. The pointer low will point to 0 and the high will point to n1(i.e. The size of arr1[]).
Calculate the ‘mid1’ i.e. x and ‘mid2’ i.e. left-x: Now, inside the loop, we will calculate the value of ‘mid1’ using the following formula:
mid1 = (low+high) // 2 ( ‘//’ refers to integer division)
mid2 = left-mid1
Calculate l1, l2, r1, and r2: Generally,
l1 = arr1[mid1-1]
l2 = arr2[mid2-1]
r1 = arr1[mid1]
r2 = arr2[mid2]
The possible values of ‘mid1’ and ‘mid2’ might be 0 and n1 and n2 respectively. So, to handle these cases, we need to store some default values for these four variables. The default value for l1 and l2 will be INT_MIN and for r1 and r2, it will be INT_MAX.
Eliminate the halves based on the following conditions:
If l1 <= r2 && l2 <= r1: We have found the answer.
If (n1+n2) is odd: Return the median = max(l1, l2).
Otherwise: Return median = (max(l1, l2)+min(r1, r2)) / 2.0
If l1 > r2: This implies that we have considered more elements from arr1[] than necessary. So, we have to take less elements from arr1[] and more from arr2[]. In such a scenario, we should try smaller values of x. To achieve this, we will eliminate the right half (high = mid1-1).
If l2 > r1: This implies that we have considered more elements from arr2[] than necessary. So, we have to take less elements from arr2[] and more from arr1[]. In such a scenario, we should try bigger values of x. To achieve this, we will eliminate the left half (low = mid1+1).
"""

def median(a: int, b: int) -> float:
    # Write the function here.
    n1,n2=len(a),len(b)
    if n1>n2:
        return median(b,a)
    n=n1+n2
    left=(n1+n2+1)//2
    low,high=0,n1
    while(low<=high):
        mid1=(low+high)//2
        mid2=left-mid1
        l1,l2,r1,r2=float('-inf'),float('-inf'),float('inf'),float('inf')
        if mid1<n1:
            r1=a[mid1]
        if mid2<n2:
            r2=b[mid2]
        if mid1-1>=0:
            l1=a[mid1-1]
        if mid2-1>=0:
            l2=b[mid2-1]
        
        if l1<=r2 and l2<=r1:
            if n%2==1:
                return float(max(l1,l2))
            else:
                return (float(max(l1,l2))+float(min(r1,r2)))/2.0
        elif l1>r2:
            high=mid1-1
        else:
            low=mid1+1
    return 0
    pass
