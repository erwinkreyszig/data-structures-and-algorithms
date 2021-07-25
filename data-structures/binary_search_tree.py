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
        else:
            return current_node
        return current_node

    def add(self, value):
        self.root = self.__add(self.root, value)


if __name__ == '__main__':
    pass



