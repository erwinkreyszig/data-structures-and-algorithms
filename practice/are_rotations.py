# -*- coding: utf-8 -*-
"""Given two strings s1 and s2, check if s2 is a rotated version of
the string s1. The characters in the strings are in lowercase.

Input:
mightandmagic
andmagicmigth
Output:
False

Input:
bananaapple
nanaappleba
Output:
True
"""


def are_rotations(str1, str2):
    str1 = list(str1)
    str2 = list(str2)
    # rotate the string len number of times by putting the first
    # character towards the end then check if the new string is the
    # same as the other string
    for i in range(len(str1)):
        tmp = str1[0]
        for j in range(len(str1) - 1):
            str1[j] = str1[j + 1]
        str1[j + 1] = tmp
        if str1 == str2:
            return True
    return False


def are_rotations_no_loop(str1, str2):
    return str2 in f'{str1}{str1}'


if __name__ == '__main__':
    str1 = 'bananaapple'
    str2 = 'nanaappleba'
    assert are_rotations(str1, str2)
    assert are_rotations_no_loop(str1, str2)
    str1 = 'mightandmagic'
    str2 = 'andmagicmigth'
    assert not are_rotations(str1, str2)
    assert not are_rotations_no_loop(str1, str2)
