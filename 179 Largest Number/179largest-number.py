class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        n = len(nums)

        for i in range(n):
            nums[i] = str(nums[i])

        for i in range(n):
            for j in range(0,n-i-1):
                if nums[j] + nums[j+1] < nums[j+1] + nums[j]:
                    nums[j] , nums[j+1] = nums[j+1] , nums[j]
        
        res = ""

        for num in nums:
            res += num
        
        return res if int(res) > 0 else "0"
