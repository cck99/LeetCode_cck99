class Solution:
    def reverseVowels(self, s: str) -> str:
        set_char = ("aeiouAEIOU")
        s = list(s)

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] not in set_char:
                left += 1
            elif s[right] not in set_char:
                right -= 1
            else:
                s[left], s[right] = s[right], s[left]
                right -= 1
                left += 1
        return "".join(s)
                
        
        