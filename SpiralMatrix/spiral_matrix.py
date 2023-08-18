from typing import List


def spiral_matrix(n: int) -> List[List[int]]:
    """
    Returns an n x n table filled with numbers from 1 to n^2 in a spiral

    Args:
        n (int): number

    Returns:
        List[List[int]]: table filled with numbers
    """

    ans = [[0] * n for _ in range(n)]

    counter = 1
    level = 0

    while counter < n * n:
        for col in range(level, n - level - 1):
            ans[level][col] = counter
            counter += 1

        for row in range(level, n - level - 1):
            ans[row][n - level - 1] = counter
            counter += 1

        for col in range(n - level - 1, level, -1):
            ans[n - level - 1][col] = counter
            counter += 1

        for row in range(n - level - 1, level, -1):
            ans[row][level] = counter
            counter += 1

        level += 1

    if n % 2 != 0:
        center = n // 2
        ans[center][center] = n * n

    return ans


matrix = spiral_matrix(1)
for r in matrix:
    print(r)


# https://leetcode.com/problems/spiral-matrix-ii/
