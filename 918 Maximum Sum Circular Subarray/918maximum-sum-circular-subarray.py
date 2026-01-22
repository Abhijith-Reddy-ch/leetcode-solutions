class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum, max_sum, min_sum = 0,0,0
        maxi = float('-inf')
        mini = float('inf')

        for i in range(n):
            total_sum += nums[i]
            max_sum += nums[i]
            min_sum += nums[i]
            maxi = max(maxi,max_sum)
            mini = min(mini,min_sum)

            if max_sum<0:
                max_sum = 0
            if min_sum>0:
                min_sum = 0
        
        if maxi<0:
                return maxi
        return max(maxi,total_sum-mini)