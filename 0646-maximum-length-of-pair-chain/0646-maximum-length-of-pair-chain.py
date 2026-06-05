class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x:x[1])
        count = 0
        last_end = float("-inf")
        for start ,end in pairs:
            if start > last_end:
                count += 1
                last_end = end
        
        return count

