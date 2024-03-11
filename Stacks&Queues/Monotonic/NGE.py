"""
Problem statement
You are given an array 'a' of size 'n'.
Print the Next Greater Element(NGE) for every element.
The Next Greater Element for an element 'x' is the first element on the right side of 'x' in the array, which is greater than 'x'.
If no greater elements exist to the right of 'x', consider the next greater element as -1.

For example:
Input: 'a' = [7, 12, 1, 20]
Output: NGE = [12, 20, 20, -1]

Explanation: For the given array,
- The next greater element for 7 is 12.
- The next greater element for 12 is 20. 
- The next greater element for 1 is 20. 
- There is no greater element for 20 on the right side. So we consider NGE as -1.

Sample Input 1:
5
1 5 3 4 2
Sample Output 1:
5 -1 4 -1 -1

Sample Input 2:
5
5 5 5 5 5
Sample Output 2:
-1 -1 -1 -1 -1
"""
def nextGreaterElement(arr: List[int], n: int) -> List[int]:
    # Write your code here.
    ans=[0]*n
    st=[]
    for i in range(n-1,-1,-1):
        if len(st)==0:
            ans[i]=-1
            st.append(arr[i])
        else:
            while st:
                if st[-1]>arr[i]:
                    ans[i]=st[-1]
                    st.append(arr[i])
                    break
                else:
                    st.pop()
            if(len(st)==0):
                ans[i]=-1
                st.append(arr[i])
    return ans
