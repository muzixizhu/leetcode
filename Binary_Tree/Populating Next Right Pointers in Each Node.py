#  Populating Next Right Pointers in Each Node
# Solution
# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:
#
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution():
    def connect(self, root):
        def dfs(node):
            if not node: return
            if root.left and root.right: root.left.next = root.right
            if root.right and root.next: root.right.next = root.next.left
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return root


class Solution_bfs:
    def connect(self, root: 'Node') -> 'Node':
        if not root:return
        tmp = [root]
        while len(tmp)>0:
            new_tmp = []
            for i in range(len(tmp)):
                if i + 1< len(tmp):
                    tmp[i].next = tmp[i+1]
                if tmp[i].left:
                    new_tmp.append(tmp[i].left)
                if tmp[i].right:
                    new_tmp.append(tmp[i].right)
            tmp = new_tmp
        return root