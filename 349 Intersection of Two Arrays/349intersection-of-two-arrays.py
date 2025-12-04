class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums2)
        common = []

        for num in nums1:
            if num in set1:
                common.append(num)
        
        common = list(set(common))
        return common