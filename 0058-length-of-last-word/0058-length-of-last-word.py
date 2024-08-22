class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        '''
        words = s.strip().split()

        if not words:
            return 0
        return len(words[-1])
        '''
        s = s.strip()
        last_index = s.rfind(' ')
        return len(s) - last_index - 1
        