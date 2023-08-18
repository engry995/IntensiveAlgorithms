from dataclasses import dataclass
from typing import Any


@dataclass
class Node:
    value: int = 0
    next: Any = None


def reverse_linked_list(node: Node) -> None:
    """
    Reverses singly linked list

    Args:
        node (Node): head of linked list
    """
    def reverse(node):
        if node.next:
            reverse(node.next)
            node.next.next = node
            node.next = None

    reverse(node)

    return

# https://leetcode.com/problems/reverse-linked-list/
