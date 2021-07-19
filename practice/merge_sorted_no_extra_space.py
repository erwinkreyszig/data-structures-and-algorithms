# -*- coding: utf-8 -*-
"""Given two sorted arrays arr1[] and arr2[] of sizes n and m
in non-decreasing order. Merge them in sorted order without
using any extra space. Modify arr1 so that it contains the first
N elements and modify arr2 so that it contains the last M elements.

Input:
n = 4, arr1[] = [1 3 5 7]
m = 5, arr2[] = [0 2 6 8 9]
Output:
arr1[] = [0 1 2 3]
arr2[] = [5 6 7 8 9]

Input:
n = 2, arr1[] = [10, 12]
m = 3, arr2[] = [5 18 20]
Output:
arr1[] = [5 10]
arr2[] = [12 18 20]
"""


def merge(arr1, arr2):
    for i, x in enumerate(arr1):
        for j, y in enumerate(arr2):
            if x > y:
                arr1[i], arr2[j] = arr2[j], arr1[i]
    return arr1, arr2


if __name__ == '__main__':
    arr1 = [1, 3, 5, 7]
    arr2 = [0, 2, 6, 8, 9]
    arr1, arr2 = merge(arr1, arr2)
    print(arr1)
    print(arr2)
