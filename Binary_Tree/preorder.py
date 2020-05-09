# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return
        res = []
        res.append(root.val)
        if self.preorderTraversal(root.left):
            res = res + self.preorderTraversal(root.left)
        if self.preorderTraversal(root.right):
            res += self.preorderTraversal(root.right)
        return res


class Solution:
    """
    @param: root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """

    def preorderTraversal(self, root):
        # write your code here
        if root is None:
            return []
        arrLeft = self.preorderTraversal(root.left)
        arrRight = self.preorderTraversal(root.right)
        return [root.val] + arrLeft + arrRight
# 更简洁

# 类似的可以实现中序遍历


class Solution_in(object):
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        arrleft = self.inorderTraversal(root.left)
        arrright = self.inorderTraversal(root.right)
        return arrleft + [root.val] + arrright


class Solution_post:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        arrleft = self.postorderTraversal(root.left)
        arrright = self.postorderTraversal(root.right)
        return arrleft + arrright + [root.val]


