# Definition for a binary tree node.
from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.LCA(root, p, q)
    
    def LCA(self, root_node = None, p = None, q = None):
        if root_node is None:
            return
        l = self.LCA(root_node.left, p, q)
        r = self.LCA(root_node.right, p, q)
        print('root_node', root_node.val)
        if p == root_node:
            return root_node
        if q == root_node:
            return root_node
        if l and r:
            return root_node
        return l or r
        
if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right = TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    
    solution = Solution()
    # print(solution.lowestCommonAncestor(root, root.left, root.right).val) # 5 1 = 3
    # print(solution.lowestCommonAncestor(root, root.left, root.left.right.right).val) # 5 4 = 5
    # print(solution.lowestCommonAncestor(root, root.left.left, root.left.right.left).val) # 6 7 5
    print(solution.lowestCommonAncestor(root, root.left, root.right) == root)
    print(solution.lowestCommonAncestor(root, root.left, root.left.right.right) == root.left)