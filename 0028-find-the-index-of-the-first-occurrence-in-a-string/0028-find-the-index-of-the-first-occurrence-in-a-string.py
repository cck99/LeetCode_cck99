class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''
        return haystack.find(needle)
        '''
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return True
        return -1