# -*- coding: utf-8 -*-
"""linked list implementation"""


class Node(object):
    def __init__(self, value=None, next=None):
        """node object requires a value"""
        if value is None:
            raise ValueError
        self.value = value
        self.next = next


class LinkedList(object):
    def __init__(self, value=None):
        """creating a LinkedList object requires an initial value for
        the head node
        initialization includes setting the next value of the
        head node to None and making the tail node be the
        same as the head node
        """
        if value is None:
            raise ValueError
        node = Node(value)
        self.head = node
        self.head.next = None
        self.tail = node

    def add_first(self, value):
        """add a node at the beginning of the list by setting the
        previous head as the new node's next value and setting
        this new node as the head
        """
        node = Node(value)
        node.next = self.head
        self.head = node

    def add_last(self, value):
        """add a node at the end of the list by setting the next
        value of the old tail node to the node to be added at the
        end and setting the tail to the new node
        """
        node = Node(value)
        self.tail.next = node
        self.tail = node
        self.tail.next = None

    def delete_first(self):
        """delete the first node of the list
        value and next attributes of the head node's next node is copied
        to head
        """
        self.head.value = self.head.next.value
        self.head.next = self.head.next.next

    def delete_last(self):
        """delete the last node in the list
        this is done by traversing the list from the head to get the
        second to the last node, each previous node is saved so that
        when the last node is reached (node with a next value of None),
        the last saved previous node will be the new tail node
        """
        node = self.head
        previous_node = None
        while(True):
            if node.next is not None:
                previous_node = node
                node = node.next
            else:
                break
        self.tail = previous_node
        self.tail.next = None

    def index_of(self, value):
        """find the index of the node that has the specified value
        iterate over the list keeping track of the nth node we are
        taking a look at, if the value matches, return the count
        if there was no match found, return -1
        """
        node = self.head
        counter = 0
        while (True):
            if node.value == value:
                return counter
            if node.next is None:
                break
            node = node.next
            counter += 1
        return -1

    def contains(self, value):
        """iterates over the list to find the one that has the
        matching value, returns True if match was found, False otherwise
        """
        return self.index_of(value) != -1

    @property
    def contents(self):
        elements = []
        current_node = self.head
        while (True):
            elements.append(current_node.value)
            if current_node.next is None:
                break
            current_node = current_node.next
        return elements

    # TODO:
    # implement insert_at(self, index, value)
    # implement delete_at(self, index)


if __name__ == '__main__':
    list = LinkedList(10)
    # test adding to last
    list.add_last(20)
    list.add_last(30)
    list.add_last(40)
    assert list.contents == [10, 20, 30, 40]
    # test adding to first
    list.add_first(9)
    list.add_first(8)
    list.add_first(7)
    assert list.contents == [7, 8, 9, 10, 20, 30, 40]
    # test element existence
    assert list.index_of(9) == 2
    assert list.index_of(50) == -1
    assert list.contains(8)
    assert not list.contains(60)
    # test deleting from first
    list.delete_first()
    list.delete_first()
    assert list.contents == [9, 10, 20, 30, 40]
    # test deleting from last
    list.delete_last()
    list.delete_last()
    assert list.contents == [9, 10, 20]
