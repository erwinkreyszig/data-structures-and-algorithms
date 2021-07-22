# -*- coding: utf-8 -*-
"""binary tree implementation
new nodes are added at the next level starting from the leftmost node
on node deletion, all children and grandchild nodes will also be removed
"""


class Node(object):

    def __init__(self, value=None):
        if value is None:
            raise ValueError('A node requires a value')
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):

    def __init__(self, root=None):
        if root is None:
            raise ValueError('A binary tree requires a noot ')
        self.root = root
        self.height = 0

    def __get_empty_branch(self, node):
        """checks whether node has branches
        returns -1 if left node is empty, this meane this node has
        no children because adding nodes go from left to right
        returns 1 if the right node is empty, this means there is a
        left child but no right child
        returns 0 if the node has both a left and right child
        """
        if node.left is None:
            return -1
        if node.right is None:
            return 1
        return 0

    def
