from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq_key = defaultdict(int)
        freq_lock = defaultdict(int)

        for ch in ransomNote:
            freq_key[ch] += 1
        
        for ch in magazine:
            freq_lock[ch] += 1

        for ch in freq_key:
            if freq_key[ch] > freq_lock[ch]:
                return False

        return True 