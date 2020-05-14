# Lowest Common Ancestor of a Binary Tree
# Solution
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
#
# Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 最低公共祖先的定义是，在一个二叉树中，我们能找到的最靠近叶子的节点，该节点同时是p和q的祖先节点。注意，如果p或者q本身也可以作为自己的祖先。
#
# 如果用递归的话，最重要的还是明白递归函数的作用是什么。这个题里面lowestCommonAncestor(root, p, q)函数的作用是判断p和q在root树中最低的公共祖先是什么，返回值是公共祖先。
#
# 这个题的模式叫做devide and conquer. 如果当前节点等于其中的p和q某一个节点，那么找到了节点，返回该节点，否则在左右子树分别寻找。
#
# 左右子树两个返回的是什么呢？按照该递归函数的定义，即找到了左子树和右子树里p和q的公共祖先，注意祖先可以是节点自己。然后根据左右侧找到的节点做进一步的判断。
#
# 如果左右侧查找的结果都不为空，说明分别找到了p和q，那么LCA就是当前节点。否则就在不为空的那个结果就是所求
# ————————————————
# 版权声明：本文为CSDN博主「负雪明烛」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/fuxuemingzhu/article/details/80778001

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right

