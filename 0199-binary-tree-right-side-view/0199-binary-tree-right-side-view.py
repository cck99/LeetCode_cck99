# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = [root]
        right_view = []

        while queue:
            lv_length = len(queue)
            for i in range(lv_length):
                node = queue.pop(0)

                if i == lv_length - 1:
                    right_view.append(node.val)
                
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return right_view
        
        '''
        result = []
        def dfs(node, depth):
            if not node:
                return
            
            if depth == len(result):
                result.append(node.val)
            
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        
        dfs(root, 0)
        return result
        '''