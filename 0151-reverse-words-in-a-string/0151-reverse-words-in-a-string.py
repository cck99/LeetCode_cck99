class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split()

        words.reverse()

        reverse_s = ' '.join(words)
        
        return reverse_s