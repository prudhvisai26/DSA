"""
Problem statement
Implement a queue data structure which follows FIFO(First In First Out) property, using only the instances of the stack data structure.
Note:
1. To implement means you need to complete some predefined functions, which are supported by a normal queue such that it can efficiently handle the given input queries which are defined below.
2. The implemented queue must support the following operations of a normal queue: 
  a. enQueue(data) : This function should take one argument of type integer and place the integer to the back of the queue.
  b. deQueue(): This function should remove an integer from the front of the queue and also return that integer. If the queue is empty, it should return -1.
  c. peek(): This function returns the element present in the front of the queue. If the queue is empty, it should return -1.
  d. isEmpty(): This function should return true if the queue is empty and false otherwise.
3. You will be given q queries of 4 types:
  a. 1 val - For this type of query, you need to insert the integer val to the back of the queue.
  b. 2 - For this type of query, you need to remove the element from the front of the queue, and also return it.
  c. 3 - For this type of query, you need to return the element present at the front of the queue(No need to remove it from the queue).
  d. 4 - For this type of query, you need to return true if the queue is empty and false otherwise.
4. For every query of type:
  a. 1, you do not need to return anything.
  b. 2, return the integer being deQueued from the queue.
  c. 3, return the integer present in the front of the queue.
  d. 4, return “true” if the queue is empty, “false” otherwise.
Example
Operations: 
1 5
1 10
2
3
4

Enqueue operation 1 5: We insert 5 at the back of the queue.
Queue: [5]

Enqueue operation 1 10: We insert 10 at the back of the queue.
Queue: [5, 10]

Dequeue operation 2: We remove the element from the front of the queue, which is 5, and print it.
Output: 5
Queue: [10]

Peek operation 3: We return the element present at the front of the queue, which is 10, without removing it.
Output: 10
Queue: [10]

IsEmpty operation 4: We check if the queue is empty.
Output: False
Queue: [10]
"""
class Queue:
    def __init__(self) -> None:
        # Initialize your data structure here.
        self.input=[]
        self.output=[]
        pass

    def enQueue(self, val: int) -> None:
        # Implement the enqueue() function.
        self.input.append(val)
        pass

    def deQueue(self) -> int:
        # Implement the dequeue() function.
        if len(self.input)==0 and len(self.output)==0:
            return -1
        if len(self.output)>0:
            return self.output.pop()
        while(self.input):
            self.output.append(self.input.pop())
        return self.output.pop()
        pass

    def peek(self) -> int:
        # Implement the peek() function here.
        if len(self.input)==0 and len(self.output)==0:
            return -1
        if len(self.output)>0:
            return self.output[-1]
        while(self.input):
            self.output.append(self.input.pop())
        return self.output[-1]
        pass

    def isEmpty(self) -> bool:
        # Implement the isEmpty() function here.
        if len(self.input)==0 and len(self.output)==0:
            return 1
        return 0
        pass
