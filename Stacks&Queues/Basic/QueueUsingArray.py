"""
Problem statement

Queue is a linear data structure that follows the idea of First In First Out. That means insertion and retrieval operations happen at opposite ends.
Implement a simple queue using arrays.
You are given 'query' queries which are either of the 2 types:

1 'e': Enqueue (add) element ‘e’ at the end of the queue.
2: Dequeue (retrieve) the element from the front of the queue. If the queue is empty, return -1.

Example:
Input: Queries: 
             [ 1 2,
               1 7,
               2,
               1 13, 
               2, 
               2, 
               2 ]
Output:
         [ 2, 
           7, 
           13,  
           -1 ]

Explanation: After each operation, our queue is equal to the following:
1 2: {2}
1 7: {2, 7}
2: {7} and 2 is printed
1 13: {7, 13}
2: {13} and 7 is printed
2: {} and 13 is printed
2: {} and -1 is printed since the queue is empty.
"""
from typing import List

class Queue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.arr= [0] * 100001
    
    #  Enqueue (add) element 'e' at the end of the queue.
    def enqueue(self, e: int) -> None:
        # Write your code here.
        if len(self.arr)==self.rear:
            return -1
        else:
            self.arr[self.rear]=e
            self.rear+=1
        pass

    #  Dequeue (retrieve) the element from the front of the queue.
    def dequeue(self) -> int:
        # Write your code here.
        if self.rear==self.front:
            return -1
        else:
            x=self.arr.pop(0)
            self.rear-=1
            return x
        pass
