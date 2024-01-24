#Merge Overlapping Sub-intervals
# Problem Statement: Given an array of intervals, merge all the overlapping intervals and return an array of non-overlapping intervals.
"""
Example 1: 
Input: intervals=[[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] are overlapping we can merge them to form [1,6]
 intervals.

Example 2:
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Since intervals [1,4] and [4,5] are overlapping we can merge them to form [1,5].
"""
#Approaches:
"""
1.Brute-Force:
    # First, we will group the closer intervals by sorting the given array of intervals(if it is not already sorted).
    # After that, we will select one interval at a time using a loop(say i) and insert it into our answer list(if the answer list is empty or the current interval cannot be merged with the last interval of the answer list). While traversing and inserting we will skip the intervals that lie in the last inserted interval of our answer list.
    # Now, for each interval arr[i], using another loop (say j) we are going to check the rest of the intervals(i.e. From index i+1 to n-1) if they can be merged with the selected interval.
    # Inside loop j, we will continue to merge all the intervals that lie in the selected interval. 
    # How to check if the current interval can be merged with the selected interval:
    # We will compare the current intervals start with the end of the selected interval. If the start is smaller or equal to the end, we can conclude the current interval can be a part of the selected interval. So, we will update the selected interval’s end with the maximum(current interval’s end, selected interval’s end) in the answer list(not in the original array).
    # We will break out of loop j, from the first element that cannot be a part of the selected interval.
    # How to check if the current interval is not a part of the selected interval:
    # We will compare the current intervals start with the end of the selected interval. If the start is greater than the end, we can conclude the current interval cannot be a part of the selected interval.
    # Finally, we will return the answer list.
    TC:O(n*logn)+O(2*N) SC:O(N)
2.Optimal Approach:
    # First, we will group the closer intervals by sorting the given array of intervals(if it is not already sorted).
    # After that, we will start traversing the array using a loop(say i) and insert the first element into our answer list(as the answer list is empty).
    # Now, while traversing we will face two different cases:
    # Case 1: If the current interval can be merged with the last inserted interval of the answer list:
        # In this case, we will update the end of the last inserted interval with the maximum(current interval’s end, last inserted interval’s end) and continue moving afterward. 
    # Case 2: If the current interval cannot be merged with the last inserted interval of the answer list:
        # In this case, we will insert the current interval in the answer array as it is. And after this insertion, the last inserted interval of the answer list will obviously be updated to the current interval.
    # Thus the answer list will be updated with the merged intervals and finally, we will return the answer list.
    TC:O(N*logn)+O(N) SC:O(n)
"""
def merge(intervals):
    ans=[]
    intervals.sort()
    for i in range(len(intervals)):
        if len(ans)==0 or intervals[i][0]>ans[-1][1]:
            ans.append(intervals[i])
        else:
            ans[-1][1]=max(ans[-1][1],intervals[i][1])
    return ans 
print(merge([[1,3],[2,6],[8,10],[15,18]]))