# -*- coding: utf-8 -*-
"""Given an array arr[ ] of size N having distinct elements, the
task is to find the next greater element for each element of the
array in order of their appearance in the array.
Next greater element of an element in the array is the nearest
element on the right which is greater than the current element.
If there does not exist next greater of current element, then next
greater element for current element is -1. For example, next greater
of the last element is always -1.

Input:
N = 4, arr[] = [1 3 2 4]
Output:
3 4 4 -1

Input:
N = 5, arr[] [6 8 0 1 3]
Output:
8 -1 1 3 -1
"""


# this solution is O(n^2)
def next_larger_element(array):
    result = []
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] < array[j]:
                result.append(array[j])
                break
        else:
            result.append(-1)
    return result


if __name__ == '__main__':
    arr = [1, 3, 2, 4]
    result = next_larger_element(arr)
    assert result == [3, 4, 4, -1]
    arr = [6, 8, 0, 1, 3]
    result = next_larger_element(arr)
    assert result == [8, -1, 1, 3, -1]
