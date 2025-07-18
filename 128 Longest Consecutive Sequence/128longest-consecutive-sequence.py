class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
         return 0
        nums.sort()
        longest = 1
        cnt = 1
        last_smaller = nums[0]
        for i in range(len(nums)):
            if nums[i] == last_smaller:
                continue  # Skip duplicates
            elif nums[i] == last_smaller + 1:
                cnt += 1
            else:
                longest = max(longest, cnt)
                cnt = 1  # Reset count
            last_smaller = nums[i]
        longest = max(longest, cnt)
        return longest