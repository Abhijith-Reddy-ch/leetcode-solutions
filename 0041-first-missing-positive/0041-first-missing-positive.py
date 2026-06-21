class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        num_set = set(nums)
        
        i = 1
        while i in num_set:
            i += 1
            
        return i
