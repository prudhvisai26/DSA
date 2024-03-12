"""
Problem statement

Implement a Stack Data Structure specifically to store integer data using two Queues.
There should be two data members, both being Queues to store the data internally. You may use the inbuilt Queue.
Implement the following public functions :

1. Constructor:
It initializes the data members(queues) as required.

2. push(data) :
This function should take one argument of type integer. It pushes the element into the stack and returns nothing.

3. pop() :
It pops the element from the top of the stack and, in turn, returns the element being popped or deleted. In case the stack is empty, it returns -1.

4. top :
It returns the element being kept at the top of the stack. In case the stack is empty, it returns -1.

5. size() :
It returns the size of the stack at any given instance of time.

6. isEmpty() :
It returns a boolean value indicating whether the stack is empty or not.
Operations Performed on the Stack:
Query-1(Denoted by an integer 1): Pushes an integer data to the stack. (push function)

Query-2(Denoted by an integer 2): Pops the data kept at the top of the stack and returns it to the caller. (pop function)

Query-3(Denoted by an integer 3): Fetches and returns the data being kept at the top of the stack but doesn't remove it, unlike the pop function. (top function)

Query-4(Denoted by an integer 4): Returns the current size of the stack. (size function)

Query-5(Denoted by an integer 5): Returns a boolean value denoting whether the stack is empty or not. (isEmpty function)
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
from typing import List
from queue import Queue

class Stack:
    def __init__(self):
        # Define the data members.
        self.q=Queue()
        pass

    def getSize(self) -> int:
        # Implement the getSize() function.
        return self.q.qsize()
        pass

    def isEmpty(self) -> bool:
        # Implement the isEmpty() function.
        return self.q.empty()
        pass

    def push(self, element: int) -> None:
        # Implement the push() function.
        s=self.q.qsize()
        self.q.put(element)
        for i in range(s):
            # print(self.q.get())
            self.q.put(self.q.get())
        pass

    def pop(self) -> int:
        # Implement the pop() function.
        if self.isEmpty():
            return -1
        return self.q.get()
        pass

    def top(self) -> int:
        # Implement the top() function.
        if self.isEmpty():
            return -1
        return self.q.queue[0]
        pass
