from typing import List


def insertion_sort(array: List[int]) -> List[int]:
    """
    Sorts the array in ascending order using insertion sort

    Args:
        array (List[int]): input

    Returns:
        List[int]: sorted array
    """

    for i in range(1, len(array)):
        elem = i
        while elem > 0 and array[elem - 1] > array[elem]:
            array[elem - 1], array[elem] = array[elem], array[elem - 1]
            elem -= 1

    return array


# https://leetcode.com/problems/sort-colors/
