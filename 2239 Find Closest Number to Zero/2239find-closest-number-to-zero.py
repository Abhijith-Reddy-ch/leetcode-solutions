class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]

        for num in nums[1:]:
            if abs(num)<abs(closest):
                closest = num
        
        if closest < 0 and abs(closest) in nums:
            return abs(closest)
        else:
            return closest