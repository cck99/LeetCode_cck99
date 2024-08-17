class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i,num in enumerate(nums):
            currect_num = target - num
            if currect_num in res:
                return [res[currect_num],i]
            
            res[num] = i

        return []

        