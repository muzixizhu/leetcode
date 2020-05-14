# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#
# Note: A leaf is a node with no children.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        ans = self.dfs(root, 1)
        return ans

    def dfs(self, node, depth):
        if not node:
            return 0
        else:
            left_dep = self.dfs(node.left, depth + 1)
            right_dep = self.dfs(node.right, depth + 1)
        return max(left_dep, right_dep) + 1

class Solution_1():
    def maxDepth(self, root):
        if not root: return 0
        return 1+ max(self.maxDepth(root.left), self.maxDepth(root.right))


class Solution_2():
    def maxDepth(self, root):
        if not root: return 0
        depth = 0
        deque = collections.deque()
        deque.append(root)
        while deque:
            node = deque.popleft()
            if not node.left or not node.right:
                depth += 1
            if not node.left:
                deque.append(node.left)
            if not node.right:
                deque.append(node.right)
        return depth