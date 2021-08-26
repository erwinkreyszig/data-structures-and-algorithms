# -*- coding: utf-8 -*-
"""Given an array arr[] of positive integers of size N.
Reverse every sub-array group of size K.

Input: arr = [1,2,3,4,5], k = 3
Output: [3,2,1,5,4]

Input: arr = [1,2,3,4,5,6,7,8,9], k = 4
Output: [4,3,2,1,8,7,6,5,9]
"""
from math import ceil, floor


def reverse_in_groups(arr, k):
    arr_len = len(arr)
    out_loop_n = ceil(arr_len / k)
    for o in range(out_loop_n):
        in_loop_n = floor(len(arr[o * k: (o + 1) * k]) / 2)
        for i in range(in_loop_n):
            left = (o * k) + i
            right = ((o + 1) * k) - i - 1
            right = arr_len - 1 - i if right > arr_len - 1 else right
            arr[left], arr[right] = arr[right], arr[left]


if __name__ == '__main__':
    results = [
        [3, 2, 1, 6, 5, 4, 9, 8, 7, 10],
        [4, 3, 2, 1, 8, 7, 6, 5, 10, 9],
        [5, 4, 3, 2, 1, 10, 9, 8, 7, 6],
        [6, 5, 4, 3, 2, 1, 10, 9, 8, 7],
    ]
    for k in range(3, 7):
        arr = [x for x in range(1, 11)]
        reverse_in_groups(arr, k)
        assert arr == results[k - 3]
