class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''c0 =c1 =c2 =0
        for i in range (len(nums)):
            if nums[i] == 0:
                c0 += 1
            elif nums[i] ==1:
                c1 += 1
            else:
                c2 += 1
        for j in range (0,c0):
            nums[j] = 0
        for k in range (c0,c0+c1):
            nums[k] = 1
        for l in range (c0+c1,c0+c1+c2):
            nums[l] = 2'''
        
        nums.sort()