# -*- coding: utf-8 -*-
"""Given two strings ‘X’ and ‘Y’, find the length of the
longest common substring.

Input : X = "abcdxyz", y = "xyzabcd"
Output : 4 "abcd"

Input : X = "zxabcdezy", y = "yzabcdezx"
Output : 6 "abcdez"
"""


def longest_common_substring(str1, str2):
    # figure out which string is shorter
    if len(str1) <= len(str2):
        base = str1
        ref = str2
    else:
        base = str2
        ref = str1
    # check if each subtsting is in the second string starting with
    # the longest one
    for i in reversed(range(1, len(base))):
        j = 0
        while j + i <= len(base):
            if base[j:i + j] in ref:
                return i, base[j:i+j]
            j += 1
    return -1


if __name__ == "__main__":
    str1 = 'abcdxyz'
    str2 = 'xyzabcd'
    assert longest_common_substring(str1, str2) == (4, 'abcd')
    str1 = 'zxabcdezy'
    str2 = 'yzabcdezx'
    assert longest_common_substring(str1, str2) == (6, 'abcdez')
    str1 = 'abcdef'
    str2 = 'ghij'
    assert longest_common_substring(str1, str2) == -1
