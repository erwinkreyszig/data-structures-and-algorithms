# -*- coding: utf-8 -*-
"""You are given N elements and your task is to Implement a Stack
in which you can get minimum element in O(1) time.

-1 will be returned if for pop() and getMin() the stack is empty.

Input:
push(2)
push(3)
pop()
getMin()  # 2
push(1)
getMin()  # 1
"""


class MinStack(object):

    def __init__(self):
        self.values = []
        self.minimums = []

    def push(self, x):
        if len(self.minimums) == 0:
            self.minimums.append(x)
        else:
            if self.minimums[-1] > x:
                self.minimums.append(x)
        self.values.append(x)


    def pop(self):
        if len(self.values) == 0:
            return -1
        x = self.values[-1]
        self.values = self.values[:-1]
        if x == self.minimums[-1]:
            self.minimums = self.minimums[:-1]
        return x

    def get_min(self):
        if len(self.minimums) == 0:
            return -1
        return self.minimums[-1]


if __name__ == '__main__':
    stack = MinStack()
    assert stack.pop() == -1
    assert stack.get_min() == -1
    stack.push(2)
    assert stack.values == [2]
    stack.push(3)
    assert stack.values == [2, 3]
    stack.pop()
    assert stack.values == [2]
    assert stack.get_min() == 2
    stack.push(1)
    assert stack.values == [2, 1]
    assert stack.get_min() == 1

