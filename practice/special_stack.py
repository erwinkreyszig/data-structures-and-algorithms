# -*- coding: utf-8 -*-
"""Design a Data Structure SpecialStack that supports all the stack
operations like push(), pop(), isEmpty(), isFull() and an additional
operation getMin() which should return minimum element from the
SpecialStack. All these operations of SpecialStack must be O(1).
To implement SpecialStack, you should only use standard Stack data
structure and no other data structure like arrays, list, . etc.
"""


class StackOperationError(Exception):
    pass

class SpecialStack(object):

    def __init__(self, size=None):
        self.__main_stack = []
        self.__sub_stack = []
        if size is None:
            raise StackOperationError('Stack size must be specified.')
        self.__size = size

    def push(self, value):
        """Insert an item into the stack."""
        if self.__get_current_size() == self.__size:
            raise StackOperationError('Adding item to a full stack.')
        self.__main_stack.append(value)
        self.__update_min_stack(value)

    def pop(self):
        """Remove an item from the stack."""
        if self.__get_current_size() == 0:
            raise StackOperationError('Removing an item from an empty stack.')
        top = self.__main_stack.pop()
        if top == self.__sub_stack[-1]:
            self.__sub_stack.pop()
        return top

    def is_empty(self):
        """Returns whether the stack is empty or not."""
        return self.__get_current_size() == 0

    def is_full(self):
        """Returns whether the stack is full or not."""
        return self.__get_current_size() == self.__size

    def get_min(self):
        """Returns the current minimum value in the stack."""
        return self.__sub_stack[-1] if len(self.__sub_stack) != 0 else -1

    def get_contents(self):
        """Returns the stack contents."""
        return self.__main_stack

    def __get_current_size(self):
        """Returns the stack's current element count"""
        return len(self.__main_stack)

    def __update_min_stack(self, value):
        """Updates the stack's sub-stack that keeps the minimum values."""
        if len(self.__sub_stack) == 0:
            self.__sub_stack.append(value)
        else:
            if value < self.__sub_stack[-1]:
                self.__sub_stack.append(value)


if __name__ == "__main__":
    stack = SpecialStack(5)
    assert stack.is_empty()
    ex = None
    try:
        stack.pop()
    except Exception as e:
        ex = e
    assert type(ex) == StackOperationError
    stack.push(18)
    stack.push(19)
    stack.push(29)
    stack.push(15)
    stack.push(16)
    assert stack.is_full()
    try:
        stack.push(1)
    except Exception as e:
        ex = e
    assert type(ex) == StackOperationError
    assert stack.get_contents() == [18, 19, 29, 15, 16]
    assert stack.get_min() == 15
    stack.pop()
    stack.pop()
    assert stack.get_contents() == [18, 19, 29]
    assert stack.get_min() == 18

