class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = s.split()
        if len(pattern) != len(arr):
            return False

        p_to_s = {}
        s_to_p = {}

        for i in range(len(pattern)):
            p = pattern[i]
            word = arr[i]

            # Check pattern → word
            if p in p_to_s and p_to_s[p] != word:
                return False

            # Check word → pattern
            if word in s_to_p and s_to_p[word] != p:
                return False

            p_to_s[p] = word
            s_to_p[word] = p

        return True
