class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()  # 将字符串 s 按空格分隔成单词列表
        if len(pattern) != len(words):
            return False  # 如果 pattern 和 s 中的元素数量不相等，直接返回 False
        
        char_to_word = {}  # 记录字符到单词的映射
        word_to_char = {}  # 记录单词到字符的映射
        
        for char, word in zip(pattern, words):
            # 检查字符到单词的映射是否一致
            if char in char_to_word:
                if char_to_word[char] != word:
                    return False
            else:
                char_to_word[char] = word
            
            # 检查单词到字符的映射是否一致
            if word in word_to_char:
                if word_to_char[word] != char:
                    return False
            else:
                word_to_char[word] = char
        
        return True
