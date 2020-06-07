Count Complete Tree Nodes
Given a complete binary tree, count the number of nodes.
Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        # if not root: return 0
        # left = self.countNodes(root.left)
        # right = self.countNodes(root.right)
        # return 1 + left + right
        if not root:
            return 0
        leftDepth = self.getDepth(root.left)
        rightDepth = self.getDepth(root.right)
        if leftDepth == rightDepth:
            return pow(2, leftDepth) + self.countNodes(root.right)
        else:
            return pow(2, rightDepth) + self.countNodes(root.left)

    def getDepth(self, root):
        if not root:
            return 0
        return 1 + self.getDepth(root.left)