class Solution:
    def isValid(self, s: str) -> bool:
        dict_ = {")":"(", "}":"{", "]":"["}
        stack = []
        
        for char in s:
            if char in dict_.values():
                stack.append(char)
            elif char in dict_.keys():
                if not stack or dict_[char] != stack.pop():
                    return False
        return not stack
        