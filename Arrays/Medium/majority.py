# Find the Majority Element that occurs more than N/2 times
# Problem Statement: Given an array of N integers, write a program to return an element that occurs more than N/2 times in the given array. You may consider that such an element always exists in the array.

"""
Example 1:
Input Format: N = 3, nums[] = {3,2,3}
Result: 3
Explanation: When we just count the occurrences of each number and compare with half of the size of the array, you will get 3 for the above solution. 

Example 2:
Input Format:  N = 7, nums[] = {2,2,1,1,1,2,2}
Result: 2
Explanation: After counting the number of times each element appears and comparing it with half of array size, we get 2 as result.

Example 3:
Input Format:  N = 10, nums[] = {4,4,2,4,3,4,4,3,2,4}
Result: 4
"""

#Approaches:
"""
1.BruteForce:
    #We will run a loop that will select the elements of the array one by one.
    #Now, for each element, we will run another loop and count its occurrence in the given array.
    #If any element occurs more than the floor of (N/2), we will simply return it.
2.Approach 1(Hashing):
    #Initialize a dictionary/hashmap and add the count of each element from the array to dictionary.
    #Finally, iterate through the hashmap and find out the element with the value >N/2 then print the result.
    TC:O(n)+O(n) Sc:O(n)
3.Approach 2(Moore's Voting Algorithm)
    #Initialise the variables count,element as zero.
    #Now run a loop and add some conditions:
        1.If count==0 then make count=1 and element=curelement.
        2.if element==currelement then increment count
        3.else decrement count
"""

#Approach 1:
def majorityElement1(nums):
    d={}
    n=len(nums)
    for i in nums:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    ans=0
    for i in d:
        if d[i]>n/2:
            ans=i
    return ans
print(majorityElement1([2,2,1,1,1,2,2]))

#Approach 2:
def majorityElement2(nums):
    count,element=0,0
    for i in nums:
        if count==0:
            count+=1
            element=i
        elif element==i:
            count+=1
        else:
            count-=1
    c=0
    for i in nums:
        if element==i:
            c+=1
    if c>len(nums)//2:
        return element
    return "No element found."
print(majorityElement2([2,2,1,1,1,2,2]))