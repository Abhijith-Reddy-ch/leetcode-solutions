class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum1 = 0
        for i  in range(0,len(nums)-1,2):
            sum1 += min(nums[i],nums[i+1])
        return sum1