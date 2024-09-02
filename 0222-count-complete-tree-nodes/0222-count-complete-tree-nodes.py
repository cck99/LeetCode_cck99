# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def getHeight(node):
            height = 0
            while node:
                node = node.left
                height += 1
            return height

        left_height = getHeight(root.left)
        right_height = getHeight(root.right)

        if left_height == right_height:
            return (1 << left_height) + countNodes(root.right)
        else:
            return (1 << right_height) + countNodes(root.left)