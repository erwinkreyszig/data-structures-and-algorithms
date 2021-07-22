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
