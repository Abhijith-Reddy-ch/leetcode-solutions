class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        freq = {}
        max_len = 0
        n = len(s)

        for r in range(n):
            freq[s[r]] = freq.get(s[r],0)+1

            while freq[s[r]] >1:
                freq[s[l]] -= 1
                l += 1

            max_len = max(max_len,r-l+1)
        return max_len