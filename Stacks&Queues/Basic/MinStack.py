"""
Problem statement
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

1. Push(num): Push the given number in the stack.
2. Pop: Remove and return the top element from the stack if present, else return -1.
3. Top: return the top element of the stack if present, else return -1.
4. getMin: Returns minimum element of the stack if present, else return -1.
For Example:

For the following input: 
1
5
1 1
1 2
4
2
3

For the first two operations, we will just insert 1 and then 2 into the stack which was empty earlier. So now the stack is => [2,1]
In the third operation, we need to return the minimum element of the stack, i.e., 1. So now the stack is => [2,1]
For the fourth operation, we need to pop the topmost element of the stack, i.e., 2. Now the stack is => [1]
In the fifth operation, we return the top element of the stack, i.e. 1 as it has one element. Now the stack is => [1]

So, the final output will be: 
1 2 1
"""

from sys import *
from collections import *
from math import *

# Implement class for minStack.
class minStack:

	# Write your code here.
			
    # Constructor
    def __init__(self):
        # Write your code here.
        self.Stack=[]
        self.Min = []
        self.mini=float('inf')
        pass
    
    # Function to add another element equal to num at the top of stack.
    def push(self, num: int) -> None:
        # Write your code here.
        if len(self.Stack)==0:
            self.Stack.append(num)
            mini=num
        if(num<self.mini):
            self.Stack.append(2*num-self.mini)
            self.mini=num
        else:
            self.Stack.append(num)
        pass
    
    # Function to remove the top element of the stack.
    def pop(self) -> int:
        # Write your code here.
        if len(self.Stack)==0:
            return -1
        elif self.mini>self.Stack[-1]:
            val=self.mini
            self.mini=2*self.mini-self.Stack[-1]
            self.Stack.pop()
            if(val==float('inf')):
                return -1
            return val
        else:
            return self.Stack.pop()
    
    # Function to return the top element of stack if it is present. Otherwise return -1.
    def top(self) -> int:
        # Write your code here.
        if len(self.Stack) == 0:
            return -1
        elif self.mini > self.Stack[-1]:
            if self.mini==float('inf'):
                return -1
            return self.mini
        else:
            return self.Stack[-1] 
        pass
    
    # Function to return minimum element of stack if it is present. Otherwise return -1.
    def getMin(self) -> int:
        # Write your code here.
        if self.mini==float('inf') or len(self.Stack)==0:
            return -1
        return self.mini
        pass
