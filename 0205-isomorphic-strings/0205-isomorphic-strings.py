class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # 两个字典用于存储字符映射关系
        s_to_t = {}
        t_to_s = {}

        for char_s, char_t in zip(s, t):
            # 检查 s 到 t 的映射
            if char_s in s_to_t:
                if s_to_t[char_s] != char_t:
                    return False
            else:
                s_to_t[char_s] = char_t

            # 检查 t 到 s 的映射
            if char_t in t_to_s:
                if t_to_s[char_t] != char_s:
                    return False
            else:
                t_to_s[char_t] = char_s

        return True
