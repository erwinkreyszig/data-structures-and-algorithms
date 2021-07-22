# -*- coding: utf-8 -*-
"""Given an array arr[] of size N and an integer K. Find the
maximum for each and every contiguous subarray of size K.


Input:
N = 9, K = 3
arr[] = 1 2 3 1 4 5 2 3 6
Output:
3 3 4 5 5 5 6

Input:
N = 10, K = 4
arr[] = 8 5 10 7 9 4 15 12 90 13
Output:
10 10 10 15 15 90 90
"""


def max_of_subarrays(arr, sub_len):
    i = 0
    out = []
    while (i + sub_len != len(arr) + 1):
        m = max(arr[i: i + sub_len])
        out.append(m)
        i += 1
    return out


def max_of_subarrays_v2(arr, sub_len):
    return [max(arr[i: i + sub_len]) for i in range(len(arr) - sub_len + 1)]


if __name__ == '__main__':
    arr1 = [1, 2, 3, 1, 4, 5, 2, 3, 6]
    k1 = 3
    res1 = [3, 3, 4, 5, 5, 5, 6]
    arr2 = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
    k2 = 4
    res2 = [10, 10, 10, 15, 15, 90, 90]
    out = max_of_subarrays(arr1, k1)
    assert out == res1
    out = max_of_subarrays(arr2, k2)
    assert out == res2
    out = max_of_subarrays_v2(arr1, k1)
    assert out == res1
    out = max_of_subarrays_v2(arr2, k2)
    assert out == res2
