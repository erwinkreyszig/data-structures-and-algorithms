# -*- coding: utf-8 -*-
"""stack implementation using python's list
if *max* value is specified when stack object is created,
stack can only accommodate *max* number of items at a time
"""


class Stack(object):

    def __init__(self, max=None):
        self.__contents = []
        self.pointer = -1
        self.__capacity = max

    def __is_empty(self):
        """determines if stack is currently empty
        returns True if it is, False otherwise"""
        return self.pointer == -1

    def __is_full(self):
        """determines if stack is full
        the check is only activated if the stack instance was created
        with a capacity value, otherwise the stack is considered infinite
        """
        if self.__capacity is not None:
            return self.__capacity - 1 == self.pointer
        return False

    def push(self, value):
        """adds an element to the stack
        checks capacity if a value was provided when the stack
        instance was created
        """
        if self.__is_full():
            raise OperationError('Stack is already full.')
        self.__contents.append(value)
        self.pointer += 1

    def pop(self):
        """returns the value at the top of the stack
        this method also removes the value from the stack
        """
        if self.__is_empty():
            raise OperationError('Stack is already empty.')
        value = self.__contents[len(self.__contents) - 1]
        del self.__contents[len(self.__contents) - 1]
        self.pointer -= 1
        return value

    @property
    def capacity(self):
        """returns the maximum number of elements the stack can hold
        a None value means infinite capacity
        """
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        """raises an exception when someone tries to change the capacity value
        """
        raise OperationError('Stack\'s capacity cannot be changed.')

    @capacity.deleter
    def capacity(self):
        """raises an exception when someone tries to delete the capacity value
        """
        raise OperationError('Stack\'s capacity value cannot be deleted.')

    @property
    def contents(self):
        """returns the contents of the stack as a list
        """
        return self.__contents

    @contents.setter
    def contents(self, value):
        """raises an exception when someone tries to modify the contents
        of the stack without using the push/pop methods
        """
        raise OperationError('Stack\'s contents cannot be changed directly. '
                             'Use push/pop methods instead.')

    @contents.deleter
    def contents(self):
        """raises an exception when someone tries to delete the contents
        of the stack
        """
        raise OperationError('Stack\'s contents cannot be deleted in one go. '
                             'Use the pop method instead.')


class OperationError(Exception):
    pass


if __name__ == '__main__':
    stack = Stack(5)
    # testing push
    stack.push(10)
    stack.push(20)
    stack.push(30)
    assert stack.contents == [10, 20, 30]
    # testing pop
    assert stack.pop() == 30
    assert stack.pop() == 20
    assert stack.contents == [10]
    # testing stack capacity
    stack.push(40)
    stack.push(50)
    stack.push(60)
    stack.push(70)
    ex = None
    try:
        stack.push(80)
    except Exception as e:
        ex = e
    assert type(ex) == OperationError
    #testing empty stack error
    for i in range(5):
        stack.pop()
    ex = None
    try:
        stack.pop()
    except Exception as e:
        ex = e
    assert type(ex) == OperationError
    # testing capacity
    assert stack.capacity == 5
    ex = None
    try:
        stack.capacity = 10
    except Exception as e:
        ex = e
    assert type(ex) == OperationError
    ex = None
    try:
        del stack.capacity
    except Exception as e:
        ex = e
    assert type(ex) == OperationError
    # testing stack content direct manipulation
    ex = None
    try:
        stack.contents = [1, 2, 3, 4, 5]
    except Exception as e:
        ex = e
    assert type(ex) == OperationError
    ex = None
    try:
        del stack.contents
    except Exception as e:
        ex = e
    assert type(ex) == OperationError
