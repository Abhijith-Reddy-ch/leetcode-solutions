from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s = list(set(nums))
        for num in s:
            ans = nums.count(num)
            if ans>len(nums)//2:
                return num
            