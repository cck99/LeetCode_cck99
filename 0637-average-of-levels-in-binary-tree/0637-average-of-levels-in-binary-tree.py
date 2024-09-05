# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:
            lv_sum = 0
            lv_count = len(queue)

            for _ in range(lv_count):
                node = queue.popleft()
                lv_sum = lv_sum + node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(lv_sum/lv_count)

        return result