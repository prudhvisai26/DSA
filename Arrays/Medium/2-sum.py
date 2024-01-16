# Two Sum : Check if a pair with given sum exists in Array
# Problem Statement: Given an array of integers arr[] and an integer target.

"""
Example 1:
Input Format: N = 5, arr[] = {2,6,5,8,11}, target = 14
Result: YES (for 1st variant)
       [1, 3] (for 2nd variant)
Explanation: arr[1] + arr[3] = 14. So, the answer is “YES” for the first variant and [1, 3] for 2nd variant.

Example 2:
Input Format: N = 5, arr[] = {2,6,5,8,11}, target = 15
Result: NO (for 1st variant)
	[-1, -1] (for 2nd variant)
Explanation: There exist no such two numbers whose sum is equal to the target.

"""
#Approaches:
"""
1.BruteForce:
    #First we will run a loop say i from 0 to n
    #Next we add a nested loop from i+1 to n
    #Then we will check whether the sum of a[i],a[j] equal to target or not.
    #If it is equal then print the pair and return true else false.
    TC:O(n^2) SC:O(1)
2.Approach 1(Hashing):
    #First we will delcare a hashmap or dictionary then start a for loop.
    #Inside the loop we check whether the target-a[i] present in the dictionary or not.
    #if yes then we return True and print the pair else false.
    TC:O(n) Sc:O(n)
3.Approach 2(2-Pointers):
    #First we sort the array, then initialize two variables i,j with 0 and n-1.
    #Now, start a while loop untill i<=j then check whether a[i]+a[j]==target
    #If so print the pair and return True. If the sum<target then increment i else increment j.
    TC: O(nlogn)+O(n) SC:O(1)
"""
#twoPointers
def twoSum(a,k):
    a.sort()
    i,j=0,len(a)-1
    while(i<=j):
        if(a[i]+a[j]==k):
            return True,[a[i],a[j]]
        elif a[i]+a[j]<k:
            i+=1
        else:
            j-=1
    return False,"No pair had found with the given sum"

print(twoSum([1,5,9,3,1,7],80))

#Hashing
def HashSum(a,k):
    n=len(a)
    d,j={},0
    for i in a:
        if k-i in d:
            return True,[i,k-i]
        d[i]=j
        j+=1
    return False,"No pair had found with the given sum"
print(HashSum([1,5,9,3,1,7],8))