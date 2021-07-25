# -*- coding: utf-8 -*-
"""Node class for tree type data structures with at most two children"""

class Node(object):

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
