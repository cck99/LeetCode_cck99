class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_num = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                currect_num = num
                currect_stack = 1

                while currect_num + 1 in nums_set:
                    currect_num = currect_num + 1
                    currect_stack = currect_stack + 1

                longest_num = max(longest_num,currect_stack)
        return longest_num