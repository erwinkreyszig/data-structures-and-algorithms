# -*- coding: utf-8 -*-
"""binary search tree implementation"""
from node import Node


class BinarySearchTree(object):

    def __init__(self, root=None):
        """initializes the tree
        an empty root node is okay
        """
        self.root = root

    def __add(self, current_node, value):
        if current_node is None:
            return Node(value)
        if current_node.value > value:
            current_node.left = self.__add(current_node.left, value)
        elif current_node.value < value:
            current_node.right = self.__add(current_node.right, value)
        return current_node

    def add(self, value):
        self.root = self.__add(self.root, value)


    def __contains(self, current_node, value):
        if current_node is None:
            return False
        if current_node.value > value:
            return self.__contains(current_node.left, value)
        elif current_node.value < value:
            return self.__contains(current_node.right, value)
        else:
            return True

    def contains(self, value):
        return self.__contains(self.root, value)

    def __delete(self, current_node, value):
        if current_node is None:
            return None
        if current_node.value > value:
            current_node.left = self.__delete(current_node.left, value)
            return current_node
        elif current_node.value < value:
            current_node.right = self.__delete(current_node.right, value)
            return current_node
        else:
            # TODO
            pass

if __name__ == '__main__':
    pass



