# -*- coding: utf-8 -*-
"""bubble sort implementation, O(n^2)

swaps adjacent elements if they are out of order
order can be set: ascending or descending
"""


def bubble_sort(input_list, order='asc'):
    n = len(input_list)
    _temp = input_list[:]
    order = order.lower()
    for i in range(n - 1):
        has_swapped = False
        for j in range(n - 1 - i):
            if (order == 'asc' and _temp[j] > _temp[j + 1]) or \
                (order == 'desc' and _temp[j] < _temp[j + 1]):
                has_swapped = True
                _temp[j], _temp[j + 1] = _temp[j + 1], _temp[j]
        if not has_swapped:
            break
    return _temp


if __name__ == '__main__':
    original_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    descending_arr = bubble_sort(original_arr, 'desc')
    assert descending_arr == [9, 8, 7, 6, 5, 4, 3, 2, 1]
    ascending_arr = bubble_sort(descending_arr)
    assert ascending_arr == original_arr
