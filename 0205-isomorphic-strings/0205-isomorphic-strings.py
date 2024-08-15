class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        '''
        indexS = [0] * 200
        indexT = [0] * 200
        
        length = len(s)

        if length != len(t): 
            return False
        
        for i in range(length): 
            if indexS[ord(s[i])] != indexT[ord(t[i])]: 
                return False
            
            indexS[ord(s[i])] = i + 1
            indexT[ord(t[i])] = i + 1
        
        return True 
        '''
        s_to_t = {}
        t_to_s = {}

        for char_s, char_t in zip(s, t):
            
            if char_s in s_to_t:
                if s_to_t[char_s] != char_t:
                    return False
            else:
                s_to_t[char_s] = char_t

            if char_t in t_to_s:
                if t_to_s[char_t] != char_s:
                    return False
            else:
                t_to_s[char_t] = char_s

        return True
