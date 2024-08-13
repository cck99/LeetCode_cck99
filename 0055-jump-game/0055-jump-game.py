class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0  # 初始化最远能到达的位置为0
        for i in range(len(nums)):  # 遍历数组的每个位置
            if i > farthest:  # 如果当前的位置 i 大于能到达的最远位置
                return False  # 说明无法到达当前的位置，返回False
            farthest = max(farthest, i + nums[i])  # 更新最远能到达的位置
        return True  # 如果能遍历完数组，说明可以到达最后的位置，返回True
