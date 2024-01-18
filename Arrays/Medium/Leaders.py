# Leaders in an Array
# Problem Statement: Given an array, print all the elements which are leaders. A Leader is an element that is greater than all of the elements on its right side in the array.

"""
Examples
Example 1:
Input:
 arr = [4, 7, 1, 0]
Output:
 7 1 0
Explanation:
 Rightmost element is always a leader. 7 and 1 are greater than the elements in their right side.

Example 2:
Input:
 arr = [10, 22, 12, 3, 0, 6]
Output:
 22 12 6
Explanation:
 6 is a leader. In addition to that, 12 is greater than all the elements in its right side (3, 0, 6), also 22 is greater than 12, 3, 0, 6.
"""

#Approaches:
"""
1.BruteForce:
    In this brute force approach, we start checking all the elements from the start of the array to the end to see if an element is greater than all the elements on its right (i.e, the leader).
    For this, we will use nested loops where the outer loop will check for each element in the array whether it is a leader or not.
    The inner loop checks if there is any element to the right that is greater than the element currently traversed by the outer loop.
    We start by initializing the outer loop pointer to the start element and setting it as the current leader.
    If any element traversed is found greater than the element currently set as a leader, it will not go to the ans array and we increment the outer loop pointer by 1 and set the next element as the current leader.
    If we don’t find any other element to the right greater than the current element, then we push the current element to the ans array stating that is it the leader element.
2.Optimal Approach:
    #If you take any array there is atmost one leader which is the last element in the array.
    #Now we initialize a max variable to last element and traverse the array from last second element to 0.
    #We check if the element is greater than max we update the max element and append that it in the new array.
    TC:O(n) Sc:O(n)
"""

def leaders(a):
    n=len(a)
    maxi=a[-1]
    b=[maxi]
    for i in range(n-2,-1,-1):
        if a[i]>maxi:
            maxi=a[i]
            b.append(maxi)
    return b
print(leaders([10,22,12,3,0,6])[::-1])