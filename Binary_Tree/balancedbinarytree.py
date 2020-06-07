Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check(node):
            if node == None:
                return (0, True)
            l_depth, l_balanced = check(node.left)
            r_depth, r_balanced = check(node.right)
            return max(l_depth, r_depth) + 1, l_balanced and r_balanced and abs(l_depth - r_depth) <= 1
        return check(root)[1]