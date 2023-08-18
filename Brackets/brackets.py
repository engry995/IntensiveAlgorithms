def are_brackets_correct(string: str) -> bool:
    """
    Accepts a string consisting only of opening and closing parentheses as input,
    and checks whether this string is correct.
    An empty string (absence of parentheses) is considered correct.

    Args:
        string (str): string to check

    Returns:
        bool: are parentheses correct
    """

    stack = []

    pair = {
        '(': ')',
        '{': '}',
        '[': ']',
    }

    for sym in string:
        if sym in pair:
            stack.append(sym)
        else:
            if not stack or sym != pair[stack.pop()]:
                return False

    return len(stack) == 0

# https://leetcode.com/problems/valid-parentheses/
