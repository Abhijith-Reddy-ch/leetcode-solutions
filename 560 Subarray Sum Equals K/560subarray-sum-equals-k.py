class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mp = {0:1}
        curr =0
        count = 0

        for x in nums:
            curr += x
            if curr -k in mp:
                count += mp[curr-k]
            mp[curr] = mp.get(curr,0)+1
        return count