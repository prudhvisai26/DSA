# Stock Buy And Sell
# Problem Statement: You are given an array of prices where prices[i] is the price of a given stock on an ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

"""
Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note: That buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""
#Approaches:
"""
1.BruteForce:
    #Use a for loop of i from 0 to n.
    #Use another for loop of j from i+1 to n.
    #If arr[j] > arr[i] , take the difference and compare  and store it in the maxPro variable.
    #Return maxPro.
    TC:O(n^2) SC:O(1)
2.Optimal Approach:
    #First create variables min,max to a[0],0
    #Then iterate through the array starting from index 0.Find out the min element for each a[i],min 
    #and then update max as max=max>min?max:min.Finally return max value.
    TC:O(n) SC:O(1) 
"""
def maxProfit(a):
    n=len(a)
    mini,maxi=a[0],0
    for i in range(n):
        if a[i]<mini:
            mini=a[i]
        maxi=max(maxi,a[i]-mini)
    return maxi
print(maxProfit([5,4,3,2,1]))