from typing import List


def bubble_sort(array: List[int]) -> List[int]:
    """
    Sorts the array in ascending order using bubble sort

    Args:
        array (List[int]): input

    Returns:
        List[int]: sorted array
    """

    for _ in range(len(array)):
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]

    return array


# https://leetcode.com/problems/sort-colors/description/
