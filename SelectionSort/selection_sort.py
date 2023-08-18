from typing import List


def selection_sort(array: List[int]) -> List[int]:
    """
    Sorts the array in ascending order using selection sort

    Args:
        array (List[int]): input

    Returns:
        List[int]: sorted array
    """

    for i in range(len(array)):
        current_min = array[i]
        current_min_idx = i
        for j in range(i + 1, len(array)):
            if array[j] < current_min:
                current_min = array[j]
                current_min_idx = j

        array[i], array[current_min_idx] = array[current_min_idx], array[i]

    return array


# https://leetcode.com/problems/sort-colors/
