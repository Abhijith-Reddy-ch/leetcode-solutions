class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt1=cnt2=0
        el1=el2=None
        n =len(nums)
            
        for num in nums:
            if el1 == num:
                cnt1 += 1
            elif el2 == num:
                cnt2 += 1
            elif cnt1 == 0:
                el1 = num
                cnt1 = 1
            elif cnt2 == 0:
                el2 = num
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        cnt1 = cnt2 = 0
        for num in nums:
            if num == el1:
                cnt1 += 1
            elif num == el2:
                cnt2 += 1

        res = []
        n = len(nums)
        if cnt1 > n // 3:
            res.append(el1)
        if cnt2 > n // 3:
            res.append(el2)

        return res