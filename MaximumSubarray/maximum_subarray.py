from typing import List


def maximum_subarray(array: List[int]) -> int:
    """
    Finds the subarray with the largest sum and returns its sum

    Args:
        array (List[int]): array

    Returns:
        int: sum
    """

    best = cur_sum = 0
    for n in array:
        cur_sum += n
        best = max(best, cur_sum)
        if cur_sum < 0:
            cur_sum = 0

    if best == 0:
        best = max(array)

    return best


# https://leetcode.com/problems/maximum-subarray/
