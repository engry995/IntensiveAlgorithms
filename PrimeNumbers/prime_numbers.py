from typing import List


def prime_numbers(n: int) -> List[int]:
    """
    Return all prime numbers from 1 to n (including)

    Args:
        n (int): number

    Returns:
        List[int]: prime numbers
    """
    limit = max(n, int(n ** (1/2)))
    numbers = [True] * (limit + 1)

    ans = []

    for i in range(2, limit + 1):
        if numbers[i]:
            ans.append(i)
            for j in range(i + 1, limit + 1):
                if j % i == 0:
                    numbers[j] = False

    return ans

# https://leetcode.com/problems/count-primes/
