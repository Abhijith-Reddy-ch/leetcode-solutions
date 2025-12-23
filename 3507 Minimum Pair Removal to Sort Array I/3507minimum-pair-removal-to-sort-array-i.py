class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ops = 0

        while nums != sorted(nums):
            mini_sum = nums[0] + nums[1]
            idx = 0

            for i in range(len(nums) - 1):
                add = nums[i] + nums[i + 1]
                if add < mini_sum:
                    mini_sum = add
                    idx = i

            nums.pop(idx)
            nums.pop(idx)
            nums.insert(idx, mini_sum)
            ops += 1

        return ops