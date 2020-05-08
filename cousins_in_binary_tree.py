# In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
#
# Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
#
# We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
#
# Return true if and only if the nodes corresponding to the values x and y are cousins.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        self.m = collections.defaultdict(tuple)
        self.dfs(root, None, 0)
        px, dx = self.m[x]
        py, dy = self.m[y]
        return dx == dy and px != py

    def dfs(self, root, parent, depth):
        if not root: return
        self.m[root.val] = (parent, depth)
        self.dfs(root.left, root, depth + 1)
        self.dfs(root.right, root, depth + 1)

class Solution():
    def __init__(self, root, x, y):
        self.m = collections.defaultdict(tuple)
        self.dfs(root, none, 0)
        px, dx = self.m[x]
        py, dy = self.m[y]
        return px != py and dx == dy

    def dfs(self, root, father, depth):
        if not root:
            return
        self.m[root.val] = (father, depth)
        self.dfs(root.left, root, depth + 1)
        self.dfs(root.right, root, depth + 1)


class Solution_2():
    def __init__(self, root, x, y):
        m = collections.defaultdict(tuple)
        q = collections.deque()
        q.append((root, None))
        depth = 0
        while q:
            size = len(q)
            for i in range(size):
                node, p = q.popleft()
                if not node: continue
                m[node.val] = (p, depth)
                q.append((node.left, node))
                q.append((node.right, node))
            depth += 1
        px, dx = m[x]
        py, dy = m[y]
        return px != py and dx == dy
