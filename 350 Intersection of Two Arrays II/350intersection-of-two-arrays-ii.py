from collections import Counter

class Solution:
    def intersect(self, nums1, nums2):
        freq1 = Counter(nums1)
        freq2 = Counter(nums2)
        common = []

        for num in freq1:
            if num in freq2:
                common.extend([num] * min(freq1[num], freq2[num]))

        return common
