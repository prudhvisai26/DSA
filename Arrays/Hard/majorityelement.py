# Majority Elements(>N/3 times) | Find the elements that appears more than N/3 times in the array
# Problem Statement: Given an array of N integers. Find the elements that appear more than N/3 times in the array. 
# If no such element exists, return an empty vector.

"""
Example 1:
Input Format: N = 5, array[] = {1,2,2,3,2}
Result: 2
Explanation: Here we can see that the Count(1) = 1, Count(2) = 3 and Count(3) = 1.Therefore, the count of 2 is greater than N/3 times. Hence, 2 is the answer.

Example 2:
Input Format:  N = 6, array[] = {11,33,33,11,33,11}
Result: 11 33
Explanation: Here we can see that the Count(11) = 3 and Count(33) = 3. Therefore, the count of both 11 and 33 is greater than N/3 times. Hence, 11 and 33 is the answer.
"""

#Approaches:
"""
1.Brute-Force:
    # We will run a loop that will select the elements of the array one by one.
    # Now, for each unique element, we will run another loop and count its occurrence in the given array.
    # If any element occurs more than the floor of (N/3), we will include it in our answer. 
    # While traversing if we find any element that is already included in our answer, we will just skip it.
    TC:O(n*2) SC:O(1)
2.Approach-1(By hashing):
    #Initialize a dictionary/hashmap and add the count of each element from the array to dictionary.
    #Finally, iterate through the hashmap and find out the element with the value >N/2 then print the result.
    TC:O(n)+O(n) Sc:O(n)
3.Approach-2:
    #Initialize 4 variables:
    # cnt1 & cnt2 :  for tracking the counts of elements
    # el1 & el2 : for storing the majority of elements.
    # Traverse through the given array.
    # If cnt1 is 0 and the current element is not el2 then store the current element of the array as el1 along with increasing the cnt1 value by 1.
    # If cnt2 is 0 and the current element is not el1 then store the current element of the array as el2 along with increasing the cnt2 value by 1.
    # If the current element and el1 are the same increase the cnt1 by 1.
    # If the current element and el2 are the same increase the cnt2 by 1.
    # Other than all the above cases: decrease cnt1 and cnt2 by 1.
    # The integers present in el1 & el2 should be the result we are expecting. So, using another loop, we will manually check their counts if they are greater than the floor(N/3).
    TC:O(n)+O(n) Sc:O(2)
"""

#Approach 1:
def majorityElement1(nums):
    d={}
    for i in nums:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    ans=[]
    # print(d)
    for i in d:
        if d[i]>len(nums)/3:
            ans.append(i)
    return ans

#Approach 2:
def majorityElement(nums):
    e1,e2,c1,c2=0,0,0,0
    for i in range(len(nums)):
        if c1==0 and e2!=nums[i]:
            c1+=1
            e1=nums[i]
        elif c2==0 and e1!=nums[i]:
            c2+=1
            e2=nums[i]
        elif e1==nums[i]:
            c1+=1
        elif e2==nums[i]:
            c2+=1
        else:
            c1-=1
            c2-=1
    res=[]
    n=len(nums)//3
    count1,count2=0,0
    for i in nums:
        if e1==i:
            count1+=1
        elif e2==i:
            count2+=1
    if count1>n:
        res.append(e1)
    if count2>n:
        res.append(e2)
    return res
print(majorityElement([11,33,33,11,33,11]))