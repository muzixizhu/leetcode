# Construct Binary Search Tree from Preorder Traversal
# Solution
# Return the root node of a binary search tree that matches the given preorder traversal.
#
# (Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)
#
# It


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not len(preorder):return None
        root = TreeNode(preorder[0])
        N = len(preorder)
        i = 1
        while i<N:
            if preorder[i]>preorder[0]:
                break
            i += 1
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root