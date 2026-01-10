from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_to_t = {}
        t_to_s = {}

        for i in range(len(s)):
            letter1 = s[i]
            letter2 = t[i]

            if letter1 in s_to_t and s_to_t[letter1] != letter2:
                return False
            if letter2 in t_to_s and t_to_s[letter2] != letter1:
                return False
            
            s_to_t[letter1] = letter2
            t_to_s[letter2] = letter1
        
        return True