class Solution:
    def isHappy(self, n: int) -> bool:
        hash_map = {}
        while n!= 1:
            if n in hash_map:
                return False
            else:
                hash_map[n] = True
                n = sum(int(digit) ** 2 for digit in str(n))
        return True