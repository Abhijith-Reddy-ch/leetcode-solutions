class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)

        add = 0
        l = 0
        ans = float('inf')
        for i in range(n):
            add += nums[i]
            while add >= target:
                ans = min(ans,i-l+1)
                add -= nums[l]
                l+=1
        return 0 if ans == float('inf') else ans