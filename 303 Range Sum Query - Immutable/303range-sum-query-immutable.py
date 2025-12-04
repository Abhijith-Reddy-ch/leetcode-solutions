class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        if not (0 <= left <= right < len(self.nums)):
            raise IndexError("Invalid range for sumRange.")
        return sum(self.nums[left : right + 1])

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)