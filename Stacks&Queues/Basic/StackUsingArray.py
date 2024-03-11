"""
Problem statement
Stack is a data structure that follows the LIFO (Last in First out) principle. Design and implement a stack to implement the following functions:
1. Push(num): Push the given number in the stack if the stack is not full.
2. Pop: Remove and print the top element from the stack if present, else print -1.
3. Top: Print the top element of the stack if present, else print -1.
4. isEmpty: Print 1 if the stack is empty, else print 0.
5. isFull: Print 1 if the stack is full, else print 0.


You have been given ‘m’ operations which you need to perform in the stack. Your task is to implement all the functions of the stack.
"""

from sys import *
from collections import *
from math import *
from typing import List

class Stack:
    def __init__(self, n: int):
        # Write your code here
        self.stack=[]
        self.capacity=n
        pass

    def push(self, num: int):
        # Write your code here
        if not self.isFull():
            self.stack.append(num)
        pass

    def pop(self) -> int:
        # Write your code here
        if not self.isEmpty():
            return self.stack.pop()
        return -1
        pass

    def top(self) -> int:
        # Write your code here
        if not self.isEmpty():
            return self.stack[-1]
        return -1
        pass

    def isEmpty(self) -> int:
        # Write your code here
        if len(self.stack)==0:
            return 1
        return 0
        pass

    def isFull(self) -> int:
        # Write your code here
        if len(self.stack)==self.capacity:
            return 1
        return 0
        pass

