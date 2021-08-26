# -*- coding: utf-8 -*-
"""merge sort implementation

divides list into halves, sorts them then collects at the end
"""


def merge_sort(input_list, order='asc'):
    order = order.lower()

    if len(input_list) > 1:
        # divide list argument into two halves
        half_point = len(input_list) // 2
        left_part = input_list[:half_point]
        right_part = input_list[half_point:]

        # divide both halves again
        merge_sort(left_part, order=order)
        merge_sort(right_part, order=order)

        # prepare counters
        left_counter = right_counter = result_counter = 0

        # overwrite input_list with sorted elements
        while left_counter < len(left_part) and right_counter < len(right_part):
            if order == 'asc':
                if left_part[left_counter] < right_part[right_counter]:
                    input_list[result_counter] = left_part[left_counter]
                    left_counter += 1
                else:
                    input_list[result_counter] = right_part[right_counter]
                    right_counter += 1
            elif order == 'desc':
                if left_part[left_counter] > right_part[right_counter]:
                    input_list[result_counter] = left_part[left_counter]
                    left_counter += 1
                else:
                    input_list[result_counter] = right_part[right_counter]
                    right_counter += 1
            result_counter += 1

        # append leftover elements
        while left_counter < len(left_part):
            input_list[result_counter] = left_part[left_counter]
            left_counter += 1
            result_counter += 1
        while right_counter < len(right_part):
            input_list[result_counter] = right_part[right_counter]
            right_counter += 1
            result_counter += 1


if __name__ == '__main__':
    input_list = [12, 11, 13, 5, 6, 7]
    merge_sort(input_list)
    assert input_list == [5, 6, 7, 11, 12, 13]
    input_list = [12, 11, 13, 5, 6, 7]
    merge_sort(input_list, 'desc')
    assert input_list == [13, 12, 11, 7, 6, 5]
