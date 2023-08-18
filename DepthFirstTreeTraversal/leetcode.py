# Definition for a binary tree node.
from typing import List
from collections import defaultdict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        graph = defaultdict(list)
        graph[root.val]

        def create_graph(vertex: TreeNode):
            if vertex.left:
                graph[vertex.val].append(vertex.left.val)
                graph[vertex.left.val].append(vertex.val)
                create_graph(vertex.left)
            if vertex.right:
                graph[vertex.val].append(vertex.right.val)
                graph[vertex.right.val].append(vertex.val)
                create_graph(vertex.right)

        create_graph(root)
        ans = []
        visited = [False] * (max(graph) + 1)

        def dfs(vertex, distance):
            visited[vertex] = True
            if distance == 0:
                ans.append(vertex)
            else:
                for neig in graph[vertex]:
                    if not visited[neig]:
                        dfs(neig, distance - 1)

        dfs(target.val, k)
        return ans
