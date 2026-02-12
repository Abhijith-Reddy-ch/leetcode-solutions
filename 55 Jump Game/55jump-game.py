class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        maxReach = 0

        for i in range(n):
            if i>maxReach:
                return False
            maxReach = max(maxReach,i+nums[i])

        return True