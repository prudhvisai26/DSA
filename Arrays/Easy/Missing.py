#Find the missing number in an array

#Problem Statement: Given an integer N and an array of size N-1 containing N-1 numbers between 1 to N. 
#Find the number(between 1 to N), that is not present in the given array.

"""
Example 1:
Input Format: N = 5, array[] = {1,2,4,5}
Result: 3
Explanation: In the given array, number 3 is missing. So, 3 is the answer.

Example 2:
Input Format: N = 3, array[] = {1,3}
Result: 2
Explanation: In the given array, number 2 is missing. So, 2 is the answer.
"""

#Approaches:
"""
1.Brute Force:
    #take an array and add the numbers up to n
    #Now run a loop and check which number is not present in array and print it.
2.Approach-1 (Sum of Natural Numbers Formula):
    #find out the sum of array elements
    #calculate the sum of natural numbers from 1 to n using n*n+1//2
    #subtract the sum of array elements from the calculated value
    #the result will be the missing number.
3.Approach-2 (using Xor):
    #find out the xor of each elements in array
    #xor all the numbers again from 1 to n
    #The xor of the final result will be zero if there are no duplicate numbers
    #otherwise, the last set bit will tell us the missing number.
"""
def find_missing_number(a,n):
    nSum=(n*(n+1))//2
    arrSum=sum(a)
    print(nSum-arrSum)

def missingNumber(a,n):
    x1,x2=0,0
    for i in range(len(a)):
        x1^=a[i]
        x2=x2^(i+1)
    x2^=n
    return x2^x1

find_missing_number([1,2,3,5],5)
print(missingNumber([1,2,3,5],5))