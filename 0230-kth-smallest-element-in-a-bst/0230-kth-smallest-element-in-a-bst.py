# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k_value = None
        self.count = 0

        def inorder(node):
            if not node or self.k_value is not  None:
                return
            
            inorder(node.left)
            
            self.count += 1
            if self.count == k:
                self.kth_value = node.val
                return
            
            inorder(node.right)
        
        inorder(root)
        return self.kth_value
                
                