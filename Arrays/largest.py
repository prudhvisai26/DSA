"""
Example 1:
Input: arr[] = {2,5,1,3,0};
Output: 5
Explanation: 5 is the largest element in the array. 

Example2: 
Input: arr[] = {8,10,5,7,9};
Output: 10
Explanation: 10 is the largest element in the array. 

"""

def largest(arr):
    largest=float('-inf');
    for i in arr:
        if i>largest:
            largest=i
    return largest

print(largest([5,10,2,3,5]))