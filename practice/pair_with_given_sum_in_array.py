# -*- coding: utf-8 -*-
"""given an unsorted array, find a pair with the given sum in it

input:
arr = [8, 7, 2, 5, 3, 1]
sum = 10

output:
8 and 2, 7 and 3

input:
arr = [5, 2, 6, 8, 1, 9]
sum = 12

output:
none
"""


def sort(arr):
    """sorts list elements in ascending order
    swaps neighboring elements if right side is larger than left side
    """
    for i in range(len(arr) - 1):
        for j in range(len(arr) - (i + 1)):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def find_pairs_for_sum(sum_var=0, arr=None):
    """sort the array (ascending) then
    get the sum starting from the outermost elements (0 and len - 1)
    if the sum is equal to the target sum, it is a pair
    if the sum is less than the target sum, move on to the next element
    from the lower side then get the sum (1 and len - 1)
    if the sum is larger than the target sum, move on to the next
    element from the upper side then get the sum (0 and len - 2)
    """
    pairs = []
    if sum_var == 0:
        return pairs
    arr = sort(arr)
    index_low, index_high = 0, len(arr) - 1
    while (index_low != index_high):
        if arr[index_low] + arr[index_high] == sum_var:
            pairs.append((arr[index_low], arr[index_high]))
            index_low += 1
        elif arr[index_low] + arr[index_high] < sum_var:
            index_low += 1
        else:
            index_high -= 1
    return pairs


if __name__ == '__main__':
    arr = [8, 7, 2, 5, 3, 1]
    sum_var = 10
    pairs = find_pairs_for_sum(sum_var, arr)
    assert (2, 8) in pairs and (3, 7) in pairs
    arr = [5, 2, 6, 8, 1, 9]
    sum_var = 12
    pairs = find_pairs_for_sum(sum_var, arr)
    assert len(pairs) == 0
