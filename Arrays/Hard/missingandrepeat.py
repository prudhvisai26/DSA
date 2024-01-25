# Find the repeating and missing numbers
# Problem Statement: You are given a read-only array of N integers with values also in the range [1, N] both inclusive. Each integer appears exactly once except A which appears twice and B which is missing. The task is to find the repeating and missing numbers A and B where A repeats twice and B is missing.

"""
Example 1:
Input Format:  array[] = {3,1,2,5,3}
Result: {3,4)
Explanation: A = 3 , B = 4 
Since 3 is appearing twice and 4 is missing

Example 2:
Input Format: array[] = {3,1,2,5,4,6,7,5}
Result: {5,8)
Explanation: A = 5 , B = 8 
Since 5 is appearing twice and 8 is missing.
"""
#Approaches:
"""
1.Brute-Force:
    # We will run a loop(say i) from 1 to N.
    # For each integer, i, we will count its occurrence in the given array using linear search.
    # We will store those two elements that have the occurrence of 2 and 0.
    # Finally, we will return the elements.
    TC:O(n*2) SC:O(1)
2.Better Approach(Hashing).
3.Optimal Approach (Using Maths):
    # First, find out the values of S and Sn and then calculate S – Sn (Using the above formulas).
    # Then, find out the values of S2 and S2n and then calculate S2 – S2n.
    # After performing steps 1 and 2, we will be having the values of X + Y and X – Y. Now, by substitution of values, we can easily find the values of X and Y.
    TC:O(n) SC:O(1)
"""
def findMissingRepeatingNumbers(a: [int]) -> [int]:
    # Write your code here
    n=len(a)
    Sn=(n*(n+1))//2
    S2n=(n*(n+1)*(2*n+1))//6
    S,S2=0,0
    for i in range(n):
        S+=a[i]
        S2+=(a[i]*a[i])
    val1=S-Sn
    val2=S2-S2n
    val2=val2//val1
    rep=(val1+val2)//2
    miss=val2-rep
    return [rep,miss]
print(findMissingRepeatingNumbers([3,1,2,5,3]))