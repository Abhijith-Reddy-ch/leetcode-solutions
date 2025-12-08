class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()   # FIX 1: sort before checking duplicates

        s1 = len(nums) * (len(nums) + 1) // 2   # FIX 2: use // to avoid float
        s2 = sum(nums)

        dup = 0
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                dup = nums[i]
                break

        ans = s1 - (s2 - dup)
        return [dup, ans]
