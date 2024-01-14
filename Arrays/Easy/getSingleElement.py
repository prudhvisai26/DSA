#Find the number that appears once, and the other numbers twice

#Problem Statement: Given a non-empty array of integers arr, every element appears twice except for one. Find that single one.
"""
Example 1:
Input Format: arr[] = {2,2,1}
Result: 1
Explanation: In this array, only the element 1 appear once and so it is the answer.

Example 2:
Input Format: arr[] = {4,1,2,1,2}
Result: 4
Explanation: In this array, only element 4 appear once and the other elements appear twice. So, 4 is the answer.
"""
#Approaches:
"""
1.BruteForce:
    #First we will run a loop then select an element and have a count with it
    #Now we will run an inner loop with j and if there is an element is euqal to selected element increment count
    #Come out of the inner loop and check whether the count is 1 or not if it just return the current element otherwise continue the loops.
    TC:O(n^2) SC:O(1)
2.Approach 1(By using Dictionary):
    #Run an loop and add the array elements in the dictionary with array element and there count.
    #Now the run the dict to find out the value of each element i.e., count.
    #If the value is 1 then print that element.
    TC:O(n)+O(n) SC:O(n)
3.Optimal (Xor Operation):
    #Initialize a variable lets say xor with 0 and find out the xor each element in the array.
    #Finally print the xor value that will be the number which would appear once.
    TC:O(n) SC:O(1)
"""
def getSingleElement(a):
    xor=0
    for i in a:
        xor^=i
    return xor
print(getSingleElement([1,1,2,2,3,4,4]))