"""
Example 1:
Input: [1,2,4,7,7,5]
Output: Second Smallest : 2
	Second Largest : 5
Explanation: The elements are as follows 1,2,3,5,7,7 and hence second largest of these is 5 and second smallest is 2

Example 2:
Input: [1]
Output: Second Smallest : -1
	Second Largest : -1
Explanation: Since there is only one element in the array, it is the largest and smallest element present in the array. There is no second largest or second smallest element present.
"""

"""
Approach:
1.Brute Force Approach(Only for non repeating elements in array): 
	# Sort the Array and print the last second and first second element.
2.Better Approach:
	# Try to find out the largest element and smallest element first in the array
    # Now again traverse through the array and find out the second largest and smallest element by a if condition
    # if(a[i]!=l and a[i]>sl);
    # if(a[i]!=s and a[i]<ss);
3.Optimal Approach (Try to do it in on traversal):
	# We would require four variables: small,second_small, large, and second_large. Variable small and second_small are initialized to INT_MAX while large and second_large are initialized to INT_MIN.
    # Now run a loop and find out the maximum and second maximum element by adding if conditions:
		* if(a[i]>maxi) if(a[i]!=l and a[i]>sl);
    	* if(a[i]<mini) if(a[i]!=s and a[i]<ss);
"""

def SecondLargest(a):
    largest,secondLargest=float("-inf"),float("-inf")
    if len(a)<=1:
        return -1
    for i in range(len(a)):
        if a[i]>largest:
            secondLargest=largest
            largest=a[i]
        if a[i]!=largest and a[i]>secondLargest:
            secondLargest=a[i]
    return secondLargest

def SecondSmallest(a):
    smallest,secondsmallest=float('inf'),float('inf')
    if len(a)<=1:
        return -1
    for i in range(len(a)):
        if a[i]<smallest:
            secondsmallest=smallest
            smallest=a[i]
        if a[i]!=smallest and a[i]<secondsmallest:
            secondsmallest=a[i]
    return secondsmallest

print(SecondLargest([0,10,8,11,13,19,14]))
print(SecondSmallest([0,10,8,11,13,19,14]))