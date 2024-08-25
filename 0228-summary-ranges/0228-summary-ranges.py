class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums == []:
            return []
        
        i = 0
        res = []

        while i < len(nums):
            start = nums[i]
            while i + 1 < len(nums) and nums[i] + 1 == nums[i+1]:
                i += 1

            if start == nums[i]:
                res.append(f'{start}')
            else:
                res.append(f'{start}->{nums[i]}')
            i+=1

        return res
