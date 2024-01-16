# Sort an array of 0s, 1s and 2s
# Problem Statement: Given an array consisting of only 0s, 1s, and 2s. Write a program to in-place sort the array without using inbuilt sort functions. ( Expected: Single pass-O(N) and constant space)

"""
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Input: nums = [2,0,1]
Output: [0,1,2]

Input: nums = [0]
Output: [0]

"""
#Approaches:
"""
1.Brute Force:
    #Simple approach sort the array.Since the array contains only 3 integers, 0, 1, and 2.
    #Simply sorting the array would arrange the elements in increasing order.
    TC:O(nlogn) SC:O(1)
2.Approach 1(using Count):
    #Initialize count valriables for 0,1,2 each as 0
    #Now run the loop and find out the number of 0s,1s and 2s in the array.
    #Run through each count likely 3 times and update the array with required values.
    TC:O(n)+O(n) SC:O(1)
3.Approach 2(using 3-Pointers):
    #Initialize 3 vars low,mid,high as 0,0,n-1 and run a loop until mid<=high
    #If arr[mid] == 0, 
        #we will swap arr[low] and arr[mid] and will increment both low and mid. Now the subarray from index 0 to (low-1) only contains 0.
    #If arr[mid] == 1, 
        #we will just increment the mid pointer and then the index (mid-1) will point to 1 as it should according to the rules.
    #If arr[mid] == 2, 
        #we will swap arr[mid] and arr[high] and will decrement high. Now the subarray from index high+1 to (n-1) only contains 2.
        In this step, we will do nothing to the mid-pointer as even after swapping, the subarray from mid to high(after decrementing high) might be unsorted. 
        So, we will check the value of mid again in the next iteration.
    TC:O(n) SC:O(1)
"""

def sortUsingCount(a):
    n=len(a)
    c0,c1,c2=0,0,0
    for i in a:
        if i==0:
            c0+=1
        elif i==1:
            c1+=1
        else:
            c2+=1
    for i in range(c0):
        a[i]=0
    for i in range(c0,c0+c1):
        a[i]=1
    for i in range(c0+c1,n):
        a[i]=2
    print(a)
sortUsingCount([0,1,2,2,1,0,0,2,1])

def sortUsingPointers(a):
    n = len(a)
    low,mid,high=0,0,n-1
    while(mid<=high):
        if(a[mid]==0):
            a[mid],a[low]=a[low],a[mid]
            low+=1
            mid+=1
        elif a[mid]==1:
            mid+=1
        else:
           a[mid],a[high]=a[high],a[mid]
           high-=1
    print(a)
sortUsingPointers([0,1,2,2,1,0,0,2,1])
 