# -*- coding: utf-8 -*-
"""dynamic array that expands to 1.5 times
its previous size when full"""


class Array(object):

    def __init__(self, length):
        """the assumption here is that the length of the container is fixed
        """
        self.container = []
        self.length = length
        self.count = 0

    def __is_full(self):
        """checks if the array is full
        returns True if it is, False otherwise
        """
        return self.count == self.length

    def __increase_capacity():
        """increases array capacity to 1.5 times its previous size
        """
        self.length = int(self.length * 1.5)
        _tmp = []
        for i, x in enumerate(self.container):
            _tmp[i] = x
        self.container = _tmp

    def __is_index_valid(self, index):
        """checks if the given index is valid
        returns True if the index is between 0 and count - 1 (inclusive),
        False otherwise
        """
        return 0 <= index <= self.count - 1

    def add(self, item):
        """adds an element at the end of the array
        first checks if the array is full, if it is, the container length
        is increased to 1.5 times its original size,
        adds the element at the end then increments the count
        if the array is not full, the item is added at the end and the
        count is incremeneted
        """
        if self.__is_full():
            self.__increase_capacity()
        self.container.append(item)
        self.count += 1

    def insert_at(self, index, item):
        """inserts the given item at the provided index
        checks validity of given index and if array is full
        if all checks return ok, the item is inserted at the specified index
        and all the others are shifted one position to the right
        """
        if not self.__is_index_valid(index):
            raise IndexError
        if self.__is_full():
            self.__increase_capacity()
        self.container.append(self.container[-1])
        for i in range(self.count - 2, index - 1, -1):
            self.container[i + 1] = self.container[i]
        self.container[index] = item
        self.count += 1

    def remove_at(self, index):
        """removes item at the given index
        if index is valid, item at index is removed and elements to the right
        are shifted one position to the left
        """
        if not self.__is_index_valid(index):
            raise IndexError
        for i in range(index, self.count - 1):
            self.container[i] = self.container[i + 1]
        self.count -= 1

    def index_of(self, item):
        """returns index of item, -1 if item is not in array
        """
        for i, x in enumerate(self.container):
            if x == item:
                return i
        return -1

    def contains(self, item):
        """returns True if the item is in the list, False otherwise"""
        return self.index_of(item) != -1

    @property
    def size(self):
        """returns the current size of the array
        """
        return self.count

    @property
    def contents(self):
        """returns the contents of the array as a list"""
        return self.container[:self.count]


if __name__ == '__main__':
    array = Array(5)
    for i in range(1, 6):
        array.add(i)
    # test array size
    assert array.size == 5
    # test item existence
    assert array.contains(2)
    assert not array.contains(6)
    # test indices
    assert array.index_of(1) == 0
    assert array.index_of(5) == 4
    assert array.index_of(3) == 2
    # test deletion
    array.remove_at(1)
    assert array.contents == [1, 3, 4, 5]
    assert array.size == 4
    array.remove_at(0)
    assert array.contents == [3, 4, 5]
    assert array.size == 3
    # test insertion
    array.insert_at(0, 10)
    assert array.contents == [10, 3, 4, 5]
    assert array.size == 4
    array.insert_at(3, 20)
    assert array.contents == [10, 3, 4, 20, 5]
    assert array.size == 5
    # test exceptions
    ex = None
    try:
        array.remove_at(100)
    except Exception as e:
        ex = e
    assert type(ex) == IndexError
    ex = None
    try:
        array.insert_at(100, 50)
    except Exception as e:
        ex = e
    assert type(ex) == IndexError
