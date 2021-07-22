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

1. does "extra space" mean I can't use any other variables or is it
restricted to "not copying contents of both arrays to a bigger array"?

"""


# doesn't work, the bottom array is not 100% sorted
def merge(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]
    return arr1, arr2


def merge_v2(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    for i in range(n + m):
        for j in range(n + m - 1):
            if j + 1 < n:
                if arr1[j] > arr1[j + 1]:
                    arr1[j], arr1[j + 1] = arr1[j + 1], arr1[j]
            elif j + 1 == n:
                if arr1[j] > arr2[j + 1 - n]:
                    arr1[j], arr2[j + 1 - n] = arr2[j + 1 - n], arr1[j]
            else:
                if arr2[j - n] > arr2[j + 1 - n]:
                    arr2[j - n], arr2[j + 1 - n] = \
                        arr2[j + 1 - n], arr2[j - n]

    return arr1, arr2


if __name__ == '__main__':
    in1_arr1 = [1, 3, 5, 7]
    in1_arr2 = [0, 2, 6, 8, 9]
    in2_arr1 = [10, 12]
    in2_arr2 = [5, 18, 20]
    r_arr1, r_arr2 = merge(in1_arr1, in1_arr2)
    assert r_arr1 == [0, 1, 2, 3]
    # error here, probably need to re-sort the lower array
    # assert r_arr2 == [5, 6, 7, 8, 9]
    r_arr1, r_arr2 = merge(in2_arr1, in2_arr2)
    assert r_arr1 == [5, 10]
    assert r_arr2 == [12, 18, 20]
    # merge v2
    r_arr1, r_arr2 = merge_v2(in1_arr1, in1_arr2)
    assert r_arr1 == [0, 1, 2, 3]
    assert r_arr2 == [5, 6, 7, 8, 9]
    r_arr1, r_arr2 = merge_v2(in2_arr1, in2_arr2)
    assert r_arr1 == [5, 10]
    assert r_arr2 == [12, 18, 20]
