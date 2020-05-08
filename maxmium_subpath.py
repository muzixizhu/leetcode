# Given a non-empty binary tree, find the maximum path sum.
#
# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.
#
# Example 1:
#
# Input: [1,2,3]
#
#        1
#       / \
#      2   3
#
# Output: 6


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self._sum = root.val

        def dfs(node):
            if not node:
                return 0
            L = dfs(node.left)
            R = dfs(node.right)
            self._sum = max(self._sum, max(L, 0) + max(R, 0) + node.val)
            return max(max(L, 0), max(0, R)) + node.val

        dfs(root)
        return self._sum
