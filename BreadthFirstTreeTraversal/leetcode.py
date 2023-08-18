# Definition for a binary tree node.
from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        ans = [[]]
        next_level = [root]

        def bfs(nodes: list[TreeNode]):
            for node in nodes:
                ans[-1].append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

        while next_level:
            ans.append([])
            current_level = next_level.copy()
            next_level.clear()
            bfs(current_level)

        return ans
