from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"TreeNode val {self.val}"


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        if left >= 0:
            left += 1
        if right >= 0:
            right += 1
        return max(left, right)


if __name__ == "__main__":
    solution = Solution()

    root = TreeNode(3)

    node_1_0 = TreeNode(9)
    node_1_1 = TreeNode(20)

    node_2_2 = TreeNode(15)
    node_2_3 = TreeNode(7)

    node_3_4 = TreeNode(97)
    node_3_5 = TreeNode(98)

    node_3_6 = TreeNode(99)
    node_3_7 = TreeNode(100)

    root.left = node_1_0
    root.right = node_1_1

    node_1_1.left = node_2_2
    node_1_1.right = node_2_3

    node_2_2.left = node_3_4
    node_2_2.right = node_3_5

    node_2_3.left = node_3_6
    node_2_3.right = node_3_7

    print(solution.maxDepth(root))
    # print(solution.maxDepth(root) == 4)
