# -*- coding: utf-8 -*-
"""queue implementation using list
"""


class Queue(object):

    def __init__(self, value=None):
        self.__contents = []
        self.__capacity = value
        self.__in_pointer = 0
        self.__out_pointer = -1

    def __is_empty(self):
        """queue empty check
        returns True if queue is empty, False otherwise
        """
        return self.__in_pointer - (self.__out_pointer + 1) == 0

    def __is_full(self):
        """queue full check
        returns True if a capacity value was set during instance
        creation and number of elements match the capacity,
        False otherwise
        """
        if self.__capacity is not None:
            return self.__in_pointer - (self.__out_pointer + 1) \
                == self.__capacity
        return False

    def queue(self, value):
        """adds a value at the end of the queue
        raises an OperationError if queue is full
        """
        if self.__is_full():
            raise OperationError('Queue is full.')
        self.__contents.append(value)
        self.__in_pointer += 1
        print(self.__out_pointer, self.__in_pointer)

    def dequeue(self):
        """removes a value at the other end of the queue
        raises an OperationError if queue is empty
        """
        if self.__is_empty():
            raise OperationError('Queue is empty.')
        _value = self.__contents[self.__out_pointer]
        self.__out_pointer += 1
        print(self.__out_pointer, self.__in_pointer)
        return _value

    @property
    def contents(self):
        """returns current contents of queue as a list
        """
        _start_at = 0 if self.__out_pointer == -1 else self.__out_pointer + 1
        return self.__contents[_start_at: self.__in_pointer]

    @contents.setter
    def contents(self, value):
        """raises an OperationError if someone tries to modify the
        contents of the queue
        """
        raise OperationError('Cannot modify queue contents directly. '
                             'Use queue/dequeue methods instead.')

    @contents.deleter
    def contents(self):
        """raises an OperationError if someone tries to delete the
        queue contents
        """
        raise OperationError('Cannot delete contents of queue. '
                             'Use dequeue isntead.')

    @property
    def capacity(self):
        """returns the queue capacity (maximum number of elements)
        """
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        """raises an OperationError if someone tries to change
        the queue's capacity value
        """
        raise OperationError('Cannot change queue capacity.')

    @capacity.deleter
    def capacity(self):
        """raises an OperationError if someone tries to delete
        the queue's capacity value
        """
        raise OperationError('Cannot delete queue capacity value.')


class OperationError(Exception):
    pass


if __name__ == '__main__':
    queue = Queue(5)
    # testing empty queue
    ex = None
    try:
        queue.dequeue()
    except Exception as e:
        ex = e
    assert type(ex) == OperationError
    # testing queue
    queue.queue(2)
    queue.queue(4)
    queue.queue(6)
    queue.queue(8)
    assert queue.contents == [2, 4, 6, 8]
    # testing full queue
    queue.queue(10)
    ex = None
    try:
        queue.queue(12)
    except Exception as e:
        ex = e
    assert type(ex) == OperationError
    assert queue.contents == [2, 4, 6, 8, 10]
    # testing dequeue
    queue.dequeue()
    queue.dequeue()
    print(queue.contents)
    assert queue.contents == [6, 8, 10]
